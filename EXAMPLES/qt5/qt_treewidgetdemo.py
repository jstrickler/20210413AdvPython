#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_treewidgetdemo import Ui_TreeWidgetDemo


class TreeWidgetDemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_TreeWidgetDemo()
        self.ui.setupUi(self)

        self._populate_tree_widget()

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)

    def _populate_tree_widget(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TreeWidgetDemoMain()
    main.show()
    sys.exit(app.exec_())
