from PyQt5.QtWidgets import QWidget, QPushButton, QLayout, QHBoxLayout, QVBoxLayout, QApplication, QDialog, QLabel
from PyQt5.QtCore import Qt


class OkCancelWidget(QWidget):
    def __init__(self, widget, orientation=Qt.Horizontal):
        super().__init__()
        self.__initUi(widget, orientation)

    def __initUi(self, widget, orientation):
        self.__okBtn = QPushButton('OK')
        self.__cancelBtn = QPushButton('Cancel')
        self.__okBtn.clicked.connect(widget.accept)
        self.__cancelBtn.clicked.connect(widget.close)

        self.__lay = ''
        if orientation == Qt.Horizontal:
            self.__lay = QHBoxLayout()
        else:
            self.__lay = QVBoxLayout()
        self.__lay.setContentsMargins(0, 0, 0, 0)
        self.__lay.addWidget(self.__okBtn)
        self.__lay.addWidget(self.__cancelBtn)
        self.__lay.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.setLayout(self.__lay)

    def setOkBtnText(self, text: str):
        self.__okBtn.setText(text)

    def setCancelBtnText(self, text: str):
        self.__cancelBtn.setText(text)

    def getOkCancelBtn(self):
        return self.__okBtn, self.__cancelBtn