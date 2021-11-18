
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('입력')
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.__wordLineEdit = QLineEdit()
        self.__wordLineEdit.textChanged.connect(self.__wordLineEditTextChanged)

        self.__okBtn = QPushButton('확인')
        self.__okBtn.clicked.connect(self.accept)

        lay = QHBoxLayout()
        lay.addWidget(self.__wordLineEdit)
        lay.addWidget(self.__okBtn)

        lay.setContentsMargins(5, 5, 5, 5)
        self.setLayout(lay)

        self.__okBtn.setEnabled(False)

    def __wordLineEditTextChanged(self):
        self.__btnToggled()

    def __btnToggled(self):
        self.__okBtn.setEnabled(self.getText().strip() != '')

    def getText(self):
        return self.__wordLineEdit.text()