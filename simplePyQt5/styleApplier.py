import os.path

from PyQt5.QtGui import QIcon


class StyleApplier:

    def __init__(self):
        self.__icon_path = 'iconPath'
        self.__style_path = 'stylePath'

    def setCssFile(self, css_file, widgets: list):
        try:
            css_file = open(css_file)
            css_code = css_file.read()
            css_file.close()
            self.setCssCode(css_code, widgets)
        except FileNotFoundError as e:
            print(e)
            print('{0} and the relative path of style caused error are not compatible with'.format(__file__))

    def setCssCode(self, css_code, widgets: list):
        for widget in widgets:
            widget.setStyleSheet(css_code)

    def setHintSize(self, widgets: list):
        for widget in widgets:
            widget.setMaximumWidth(widget.sizeHint().width())
            widget.setMaximumHeight(widget.sizeHint().height())

    def setIconPath(self, icon_path):
        self.__icon_path = icon_path

    def setStylePath(self, style_path):
        self.__style_path = style_path

    def setIconAutomatically(self, token: list, widgets: list):
        for i in range(len(widgets)):
            widgets[i].setIcon(QIcon(self.__icon_path + token[i] + '.png'))

    def setToolTip(self, texts: list, widgets: list):
        for i in range(len(widgets)):
            widgets[i].setToolTip(texts[i])
