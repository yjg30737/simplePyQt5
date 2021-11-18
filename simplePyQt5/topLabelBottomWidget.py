from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt

from simplePyQt5.verticalWidget import VerticalWidget
from simplePyQt5.topLeftRightWidget import TopLeftRightWidget


class TopLabelBottomWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        self.__bottomWidget = TopLeftRightWidget()

        self.__lbl = QLabel('')

        mainWidget = VerticalWidget()
        mainWidget.addWidgets([self.__lbl, self.__bottomWidget])
        lay = mainWidget.layout()

        self.setLayout(lay)

    def setLabel(self, text: str):
        self.__lbl.setText(text)

    def setLeftWidgets(self, widgets: list, align=Qt.AlignVCenter):
        self.__bottomWidget.setLeftWidgets(widgets, align=align)

    def setRightWidgets(self, widgets: list, align=Qt.AlignVCenter):
        self.__bottomWidget.setRightWidgets(widgets, align=align)

    def addBottomWidget(self, widget):
        self.__bottomWidget.addBottomWidget(widget)