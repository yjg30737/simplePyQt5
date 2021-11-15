from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt


class LeftRightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._initUi()

    def _initUi(self):
        self._gridLayout = QGridLayout()
        self._gridLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._gridLayout)

    def setLeftWidgets(self, widgets, align=Qt.AlignVCenter):
        leftWidget = QWidget()
        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignLeft | align)
        lay.setContentsMargins(0, 0, 0, 0)
        for widget in widgets:
            lay.addWidget(widget)
        leftWidget.setLayout(lay)
        self._gridLayout.addWidget(leftWidget, 0, 0, 1, 1)

    def setRightWidgets(self, widgets, align=Qt.AlignVCenter):
        rightWidget = QWidget()
        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignRight | align)
        lay.setContentsMargins(0, 0, 0, 0)
        for widget in widgets:
            lay.addWidget(widget)
        rightWidget.setLayout(lay)
        self._gridLayout.addWidget(rightWidget, 0, 1, 1, 1)

    def getLeftWidget(self):
        return self._gridLayout.itemAtPosition(0, 0).widget()

    def getRightWidget(self):
        return self._gridLayout.itemAtPosition(0, 1).widget()

    def setLeftMargin(self, margin: int):
        self.getLeftWidget().layout().setContentsMargins(margin, 0, 0, 0)

    def setRightMargin(self, margin: int):
        self.getRightWidget().layout().setContentsMargins(0, 0, margin, 0)
