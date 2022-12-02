import sys
from PyQt5 import QtWidgets
import psycopg2
import nltk
import main_window, widget
import spacy
import re
from googletrans import Translator
from nltk.tokenize import sent_tokenize
import pyodbc

con = pyodbc.connect('Driver={SQL Server};'
                      'Server=VALIANTSIN-PC;'
                      'Database=EYAZIS;'
                      'Trusted_Connection=yes;')


class Dialog(QtWidgets.QDialog, widget.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Application(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    word_tf = {}
    word_info = {}

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dialog = None
        self.chooseFileButton.clicked.connect(self.browse_file)
        self.addDictButton.clicked.connect(self.add_to_dict)
        self.deleteDictButton.clicked.connect(self.delete_dict)
        self.translateDictButton.clicked.connect(self.translate_dict)
        self.saveButton.clicked.connect(self.save_file)
        self.viewInfoButton.clicked.connect(self.get_information)
        self.treeDraw.clicked.connect(self.draw)

    def draw(self):
        num = int(self.lineEdit.text())
        simple_grammar = """NP: {<DT>?<JJ>*<NN>}
                           VBD: {<VBD>}
                           IN: {<IN>}"""
        parser_chunking = nltk.RegexpParser(simple_grammar)
        text = self.originalText.toPlainText()
        sentences = sent_tokenize(text)
        # sent_text = nltk.word_tokenize(sents)
        pos_text = nltk.pos_tag(sentences[num - 1].split())
        parser_chunking.parse(pos_text)
        Output_chunk = parser_chunking.parse(pos_text)
        Output_chunk.draw()

    def browse_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл', "*.txt")[0]
        if file:
            openfile = open(file, 'r')
            with openfile:
                self.originalText.setText(openfile.read())

    def translate_dict(self):
        self.word_info = {}
        self.word_tf = {}
        words_count = 0
        nlp = spacy.load("en_core_web_sm")
        text = self.originalText.toPlainText()
        data = {
            'sourceLanguageCode': 'en',
            'targetLanguageCode': 'fr',
            'texts': text,
        }
        words = self.get_words(text)
        print(words)
        self.sourceTextValueLabel.setText(str(len(words)))
        print('Words in source text:' + str(len(words)))
        self.word_tf = self.get_tf(words)
        cur = con.cursor()
        cur.execute("SELECT * FROM dict")
        for row in cur:
            result = re.findall(row[1], text, re.IGNORECASE)
            if result:
                words_count += len(result)
                word = nlp(result[0])
                for token in word:
                    self.word_info[token.text] = row[2] + ' ' + token.lemma_ + ' ' + token.pos_
                    # print('hi')
                text = re.sub(row[1], row[2], text, flags=re.IGNORECASE)
        cur.close()
        self.send(data)

    def get_information(self):
        sfile = open('share/words_info.html', 'w', encoding="utf-8")
        with sfile:
            sfile.write("""
                    <!doctype html>
            <html>
            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
                <div>
                    """)
            sfile.write('Частота слов:<br>')
            for word, tf in self.word_tf.items():
                sfile.write(word + ' - ' + str(tf) + "<br>")
            # sfile.write(str(self.word_tf))
            sfile.write('************ <br>')
            sfile.write('Информация о словах из словаря:<br>')
            sfile.write('************ <br>')
            if len(self.word_info) == 0:
                sfile.write('Совпадений со словарем не обнаружено<br>')
            else:
                for word, info in self.word_info.items():
                    sfile.write(word + ' - ' + info + '<br>')
            sfile.write(str(self.word_info))

            sfile.write("""
                    </div>
                </body>
            </html>
                    """)

    def send(self, data):
        translator = Translator()
        response = translator.translate(data["texts"], dest=data["targetLanguageCode"])
        self.translatedText.setText(response.text)
        self.targetTextValueLabel.setText(str(len(self.get_words(response.text))))
        print('Words in target text: ' + str(len(self.get_words(response.text))))

    def get_words(self, text):
        words = {}
        for raw_word in text.split():
            if raw_word.endswith((',', '.', '-', '!', '?', ';', '»', ')', '”', ':')):
                raw_word = raw_word[:-1]
            if raw_word.startswith(('«', '(', '“')):
                raw_word = raw_word[1:]
            word = raw_word
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        return words

    def get_tf(self, words):
        max_count = 0
        for count in words.values():
            max_count += count
        tf_dict = {}
        for word in words:
            tf_dict[word] = round(words[word] / max_count, 4)
        sorted_tf_dict = {key: v for key, v in sorted(tf_dict.items(), key=lambda item: item[1], reverse=True)}
        return sorted_tf_dict

    def add_to_dict(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл', "*.txt")[0]
        cur = con.cursor()
        if file_name:
            openfile = open(file_name, 'r', encoding='utf-8')
            with openfile:
                for line in openfile:
                    line_words = line.split(' - ')
                    query= f"INSERT INTO [dbo].[dict] (engwrd,frewrd) VALUES ('{line_words[0]}','{line_words[1][:-1]}')"
                    print(query)
                    cur.execute(query)
                    con.commit()
        cur.close()
        self.dialog = Dialog()
        self.dialog.show()
        self.dialog.textEdit.setText('Записи были добавлены')

    def delete_dict(self):
        cur = con.cursor()
        cur.execute("DELETE FROM dict")
        cur.close()
        self.dialog = Dialog()
        self.dialog.show()
        self.dialog.textEdit.setText('Записи удалены')

    def save_file(self):
        text = self.translatedText.toPlainText()
        html = "<p>" + text.replace("\n", "<br>") + "</p>"
        sfile = open('share/translated.html', 'w', encoding="utf-8")
        with sfile:
            sfile.write("""
            <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <div>
            """)
            sfile.write(html)

            sfile.write("""
            </div>
        </body>
    </html>
            """)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
