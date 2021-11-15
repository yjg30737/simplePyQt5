from PyQt5.QtWidgets import QWidget, QFrame, QGridLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class GeneralHorizontalWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self._initUi(parent=parent)

    def _initUi(self, parent=None):
        self._hboxLayout = QHBoxLayout(parent)
        self._hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._hboxLayout)

    def add_widget(self, widget, align=Qt.AlignLeft):
        self._hboxLayout.addWidget(widget)
        self._set_attr_of_layout(align=align)

    def addSeparator(self, base_style=QFrame.Sunken, css_style='', width=1):
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(base_style)
        line.setMaximumWidth(width)
        line.setContentsMargins(0, 0, 0, 0)
        self._hboxLayout.addWidget(line)
        if css_style:
            pass
        else:
            css_style = 'border: 1px solid #DDD;'
        line.setStyleSheet(css_style)

    def add_widgets(self, widgets: list, align=Qt.AlignLeft, separator_css_style=''):
        for widget in widgets:
            if widget:
                self.add_widget(widget, align=align)
            else:
                self.addSeparator(css_style=separator_css_style)

    def insert_widget(self, widget, idx=0, align=Qt.AlignLeft):
        self._hboxLayout.insertWidget(idx, widget)
        self._set_attr_of_layout(align=align)

    def insertSeparator(self, idx, base_style=QFrame.Sunken, css_style='', width=1):
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(base_style)
        line.setMaximumWidth(width)
        line.setContentsMargins(0, 0, 0, 0)
        self._hboxLayout.insertWidget(idx, line)
        if css_style:
            pass
        else:
            css_style = 'border: 1px solid #DDD;'
        line.setStyleSheet(css_style)

    def insert_widgets(self, widgets: list, idx=0, align=Qt.AlignLeft, separator_css_style=''):
        for widget in widgets:
            if widget:
                self.insert_widget(widget, idx=idx, align=align)
            else:
                self.insertSeparator(idx=idx, css_style=separator_css_style)

    def _set_attr_of_layout(self, align):
        if self.layout():
            self.layout().setAlignment(align)
            self.layout().setContentsMargins(0, 0, 0, 0)

    def setReasonableMaximumHeight(self):
        max_height = max([self.layout().itemAt(i).widget().sizeHint().height() for i in range(self.layout().count())])
        for i in range(self.layout().count()):
            self.layout().itemAt(i).widget().setMinimumHeight(max_height)

    def setStyleSheet(self, styleSheet: str) -> None:
        super().setStyleSheet(styleSheet)
