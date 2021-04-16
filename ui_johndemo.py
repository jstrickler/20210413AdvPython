# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'johndemo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JohnDemo(object):
    def setupUi(self, JohnDemo):
        JohnDemo.setObjectName("JohnDemo")
        JohnDemo.resize(411, 177)
        self.centralwidget = QtWidgets.QWidget(JohnDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        JohnDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JohnDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        JohnDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JohnDemo)
        self.statusbar.setObjectName("statusbar")
        JohnDemo.setStatusBar(self.statusbar)
        self.actionCopy = QtWidgets.QAction(JohnDemo)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(JohnDemo)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCut = QtWidgets.QAction(JohnDemo)
        self.actionCut.setObjectName("actionCut")
        self.actionUndo = QtWidgets.QAction(JohnDemo)
        self.actionUndo.setObjectName("actionUndo")
        self.actionDoOver = QtWidgets.QAction(JohnDemo)
        self.actionDoOver.setObjectName("actionDoOver")
        self.actionQuit = QtWidgets.QAction(JohnDemo)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionDoOver)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(JohnDemo)
        self.actionQuit.triggered.connect(JohnDemo.close)
        QtCore.QMetaObject.connectSlotsByName(JohnDemo)

    def retranslateUi(self, JohnDemo):
        _translate = QtCore.QCoreApplication.translate
        JohnDemo.setWindowTitle(_translate("JohnDemo", "John Demo for Adv Python Class"))
        self.label_2.setText(_translate("JohnDemo", "Personal Information"))
        self.label.setText(_translate("JohnDemo", "Enter your name"))
        self.menuFile.setTitle(_translate("JohnDemo", "File"))
        self.menuEdit.setTitle(_translate("JohnDemo", "Edit"))
        self.actionCopy.setText(_translate("JohnDemo", "Copy"))
        self.actionPaste.setText(_translate("JohnDemo", "Paste"))
        self.actionCut.setText(_translate("JohnDemo", "Cut"))
        self.actionUndo.setText(_translate("JohnDemo", "Undo"))
        self.actionDoOver.setText(_translate("JohnDemo", "Redo"))
        self.actionQuit.setText(_translate("JohnDemo", "Quit"))

