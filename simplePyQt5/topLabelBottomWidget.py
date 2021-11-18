from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt

from verticalWidget import VerticalWidget
from topLeftRightWidget import TopLeftRightWidget


class TopLabelBottomWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        self.__bottomWidget = TopLeftRightWidget()

        self.__lbl = QLabel('')

        mainWidget = VerticalWidget()
        mainWidget.add_widgets([self.__lbl, self.__bottomWidget])
        lay = mainWidget.layout()

        self.setLayout(lay)

    def setLabel(self, text: str):
        self.__lbl.setText(text)

    def setLeftWidgets(self, widgets: list, align=Qt.AlignVCenter):
        self.__bottomWidget.set_left_widgets(widgets, align=align)

    def setRightWidgets(self, widgets: list, align=Qt.AlignVCenter):
        self.__bottomWidget.set_right_widgets(widgets, align=align)

    def addBottomWidget(self, widget):
        self.__bottomWidget.add_bottom_widget(widget)