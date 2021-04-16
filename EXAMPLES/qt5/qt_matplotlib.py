#!/usr/bin/env python
import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_matplotlibdemo import Ui_MatplotlibDemo


class MatplotlibDemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_MatplotlibDemo()
        self.ui.setupUi(self)

        self.ui.bt_plot.clicked.connect(self._plot)
        self.ui.bt_clear.clicked.connect(self._clear)

    def _plot(self):
        data = [random.randint(1, 100) for _ in range(100)]
        self.ui.mpl_widget.ax.plot(data)
        self.ui.mpl_widget.canvas.draw()

    def _clear(self):
        self.ui.mpl_widget.ax.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MatplotlibDemoMain()
    main.show()
    sys.exit(app.exec_())
