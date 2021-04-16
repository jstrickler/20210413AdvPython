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
        JohnDemo.resize(228, 174)
        self.centralwidget = QtWidgets.QWidget(JohnDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        JohnDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JohnDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 22))
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
        self.actionRedo = QtWidgets.QAction(JohnDemo)
        self.actionRedo.setObjectName("actionRedo")
        self.actionQuit = QtWidgets.QAction(JohnDemo)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(JohnDemo)
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
        self.actionRedo.setText(_translate("JohnDemo", "Redo"))
        self.actionQuit.setText(_translate("JohnDemo", "Quit"))

