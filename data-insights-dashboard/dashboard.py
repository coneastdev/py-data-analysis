import sys
import time

import numpy as np

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QInputDialog, QFileDialog

from matplotlib.backends.backend_qtagg import FigureCanvas # pyright: ignore[reportAttributeAccessIssue]
from matplotlib.backends.backend_qt import \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.qt_compat import QtWidgets # pyright: ignore[reportAttributeAccessIssue]
from matplotlib.figure import Figure


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        titleLable = QLabel("DATA INSIGHTS DASHBOARD")
        titleLableFont = titleLable.font()
        titleLableFont.setPointSize(30)
        titleLable.setFont(titleLableFont)
        titleLable.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        layout.addWidget(titleLable)

if __name__ == "__main__":
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec()