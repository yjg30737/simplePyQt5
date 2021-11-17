from PyQt5.QtWidgets import QFrame
from leftRightWidget import LeftRightWidget


class TopLeftRightWidget(LeftRightWidget):
    def __init__(self):
        super().__init__()

    def _initUi(self):
        super()._initUi()

    # make set bottom widgets to clear all bottom widgets and make new widget given by arg
    def setBottomWidget(self, widget):
        self._gridLayout.addWidget(widget, self._gridLayout.rowCount(), 0, 1, 2)

    def addBottomWidget(self, widget):
        self._gridLayout.addWidget(widget, self._gridLayout.rowCount(), 0, 1, 2)

    def addSeparator(self, base_style=QFrame.Sunken, css_style='', height=1):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(base_style)
        line.setMaximumHeight(height)
        self._gridLayout.addWidget(line, self._gridLayout.rowCount(), 0, 1, 2)

        if css_style:
            line.setStyleSheet(css_style)

