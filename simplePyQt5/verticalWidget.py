from PyQt5.QtWidgets import QWidget, QFrame, QGridLayout, QSizePolicy, QVBoxLayout
from PyQt5.QtCore import Qt


class VerticalWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._initUi(parent=parent)

    def _initUi(self, parent=None):
        self._vboxLayout = QVBoxLayout(parent)
        self._vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._vboxLayout)

    def addWidget(self, widget, align=Qt.AlignTop):
        self._vboxLayout.addWidget(widget)
        if align:
            self._setAttrOfLayout(align=align)

    def addSeparator(self, base_style=QFrame.Sunken, css_style='', height=1):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(base_style)
        line.setContentsMargins(0, 0, 0, 0)
        line.setMaximumHeight(height)
        self._vboxLayout.addWidget(line)
        if css_style:
            pass
        else:
            css_style = 'border: 1px solid #DDD;'
        line.setStyleSheet(css_style)

    def addWidgets(self, widgets: list, align=Qt.AlignTop, separator_css_style=''):
        for widget in widgets:
            if isinstance(widget, QWidget):
                self.addWidget(widget, align=align)
            else:
                self.addSeparator(css_style=separator_css_style)

    def insertWidget(self, widget, idx, align=Qt.AlignTop):
        self._vboxLayout.insertWidget(idx, widget)
        if align:
            self._setAttrOfLayout(align=align)

    def insertSeparator(self, idx=0, base_style=QFrame.Sunken, css_style='', height=1):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(base_style)
        line.setContentsMargins(0, 0, 0, 0)
        line.setMaximumHeight(height)
        self._vboxLayout.insertWidget(idx, line)
        if css_style:
            pass
        else:
            css_style = 'border: 1px solid #DDD;'
        line.setStyleSheet(css_style)

    def _setAttrOfLayout(self, align):
        if self.layout():
            self.layout().setAlignment(align)
            self.layout().setContentsMargins(0, 0, 0, 0)