# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(3, 10, 700, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(100, 0, 10, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.translateDictButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.translateDictButton.setObjectName("translateDictButton")
        self.gridLayout.addWidget(self.translateDictButton, 0, 1, 1, 1)
        self.chooseFileButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chooseFileButton.setObjectName("chooseFileButton")
        self.gridLayout.addWidget(self.chooseFileButton, 0, 0, 1, 1)
        self.deleteDictButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteDictButton.setObjectName("deleteDictButton")
        self.gridLayout.addWidget(self.deleteDictButton, 0, 2, 1, 1)
        self.addDictButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addDictButton.setObjectName("addDictButton")
        self.gridLayout.addWidget(self.addDictButton, 1, 0, 1, 1)
        self.viewInfoButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.viewInfoButton.setObjectName("viewInfoButton")
        self.gridLayout.addWidget(self.viewInfoButton, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.originalText = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.originalText.setObjectName("originalText")
        self.verticalLayout.addWidget(self.originalText)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.translatedText = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.translatedText.setObjectName("translatedText")
        self.verticalLayout.addWidget(self.translatedText)
        self.upperHorizontalLayout = QtWidgets.QHBoxLayout()
        self.upperHorizontalLayout.setObjectName("upperHorizontalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.treeDraw = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.treeDraw.setObjectName("treeDraw")
        self.horizontalLayout.addWidget(self.treeDraw)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.upperHorizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.upperHorizontalLayout)
        self.sourceTextAmountLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sourceTextAmountLabel.setObjectName("sourceTextAmountLabel")
        self.upperHorizontalLayout.addWidget(self.sourceTextAmountLabel)
        self.sourceTextValueLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sourceTextValueLabel.setObjectName("sourceTextValueLabel")
        self.upperHorizontalLayout.addWidget(self.sourceTextValueLabel)
        self.targetTextAmountLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.targetTextAmountLabel.setObjectName("targetTextAmountLabel")
        self.upperHorizontalLayout.addWidget(self.targetTextAmountLabel)
        self.targetTextValueLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.targetTextValueLabel.setObjectName("targetTextAmountLabel")
        self.upperHorizontalLayout.addWidget(self.targetTextValueLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Qt5"))
        self.translateDictButton.setText(_translate("MainWindow", "Перевод"))
        self.chooseFileButton.setText(_translate("MainWindow", "Загрузить текст"))
        self.deleteDictButton.setText(_translate("MainWindow", "Удалить словарь"))
        self.addDictButton.setText(_translate("MainWindow", "Создать словарь"))
        self.viewInfoButton.setText(_translate("MainWindow", "Статистика перевода"))
        self.label_2.setText(_translate("MainWindow", "Исходный текст:"))
        self.label.setText(_translate("MainWindow", "Перевод:"))
        self.sourceTextAmountLabel.setText(_translate("MainWindow", "Количество слов в исходном:"))
        self.targetTextAmountLabel.setText(_translate("MainWindow", "Количество слов в переведенном:"))
        self.sourceTextValueLabel.setText(_translate("MainWindow", "0"))
        self.targetTextValueLabel.setText(_translate("MainWindow", "0"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить перевод"))
        self.treeDraw.setText(_translate("MainWindow", "Вывести дерево"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
