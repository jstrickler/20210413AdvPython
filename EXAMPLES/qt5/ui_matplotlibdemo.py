# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matplotlibdemo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MatplotlibDemo(object):
    def setupUi(self, MatplotlibDemo):
        MatplotlibDemo.setObjectName("MatplotlibDemo")
        MatplotlibDemo.resize(879, 481)
        self.centralwidget = QtWidgets.QWidget(MatplotlibDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.mpl_widget = MplWidget(self.centralwidget)
        self.mpl_widget.setGeometry(QtCore.QRect(40, 20, 801, 321))
        self.mpl_widget.setObjectName("mpl_widget")
        self.bt_plot = QtWidgets.QPushButton(self.centralwidget)
        self.bt_plot.setGeometry(QtCore.QRect(80, 370, 113, 32))
        self.bt_plot.setObjectName("bt_plot")
        self.bt_quit = QtWidgets.QPushButton(self.centralwidget)
        self.bt_quit.setGeometry(QtCore.QRect(620, 370, 113, 32))
        self.bt_quit.setObjectName("bt_quit")
        self.bt_clear = QtWidgets.QPushButton(self.centralwidget)
        self.bt_clear.setGeometry(QtCore.QRect(340, 370, 113, 32))
        self.bt_clear.setObjectName("bt_clear")
        MatplotlibDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MatplotlibDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MatplotlibDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MatplotlibDemo)
        self.statusbar.setObjectName("statusbar")
        MatplotlibDemo.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MatplotlibDemo)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MatplotlibDemo)
        self.actionQuit.triggered.connect(MatplotlibDemo.close)
        self.bt_quit.clicked.connect(MatplotlibDemo.close)
        QtCore.QMetaObject.connectSlotsByName(MatplotlibDemo)

    def retranslateUi(self, MatplotlibDemo):
        _translate = QtCore.QCoreApplication.translate
        MatplotlibDemo.setWindowTitle(_translate("MatplotlibDemo", "Matplotlib Demo with Titanic Data"))
        self.bt_plot.setText(_translate("MatplotlibDemo", "Plot"))
        self.bt_quit.setText(_translate("MatplotlibDemo", "Quit"))
        self.bt_clear.setText(_translate("MatplotlibDemo", "Clear"))
        self.menuFile.setTitle(_translate("MatplotlibDemo", "File"))
        self.actionQuit.setText(_translate("MatplotlibDemo", "Quit"))

from mplwidget import MplWidget
