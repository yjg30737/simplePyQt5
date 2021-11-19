import sys

from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QTableWidgetItem, QWidget
from PyQt5.QtCore import Qt

from simplePyQt5.horizontalWidget import HorizontalWidget


class TableWidget(QTableWidget):
    __horizontal_header = []
    __vertical_header = []

    def __init__(self, parent=None):
        super().__init__(parent)
        self._initUi()

    def _initUi(self):
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def setHorizontalHeaderLabels(self, lst):
        self.horizontalHeader().setVisible(True)
        self.__horizontal_header = lst
        self.setColumnCount(len(lst))
        super().setHorizontalHeaderLabels(lst)
        self.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

    def setVerticalHeaderLabels(self, lst, align=Qt.AlignCenter):
        self.verticalHeader().setVisible(True)
        self.__vertical_header = lst
        self.setRowCount(len(lst))
        super().setVerticalHeaderLabels(lst)
        self.verticalHeader().setDefaultAlignment(Qt.AlignCenter)

    def clearRows(self):
        for i in range(self.rowCount(), -1, -1):
            self.removeRow(i)

    def removeRow(self, row: int) -> None:
        super().removeRow(row)

    def removeSelectedRows(self):
        indexes = self.selectedIndexes()
        if indexes:
            for i in range(len(indexes)-1, -1, -1):
                self.removeRow(indexes[i].row())

    def _insertItem(self, args: iter, r_idx=0, c_idx=0, align=Qt.AlignVCenter, ifExistsFunc=None, duplicated_enabled=False):
        if isinstance(args[0], QWidget):
            self._insertTableWidgetRow(args, r_idx=r_idx, c_idx=c_idx, align=align)
        else:
            key = args[0].text() if isinstance(args[0], QTableWidgetItem) else args[0]
            items = '' if duplicated_enabled else self.findItems(key, Qt.MatchFixedString)
            if not items:
                self._insertTableWidgetRow(args, r_idx=r_idx, c_idx=c_idx, align=align)
            else:
                if ifExistsFunc:
                    ifExistsFunc()
                else:
                    pass

    def _setItem(self, args: iter, align=Qt.AlignVCenter, ifExistsFunc=None, duplicated_enabled=False):
        try:
            if isinstance(args[0], QWidget):
                self._setTableWidgetRow(args, align=align)
            else:
                if isinstance(args[0], dict):
                    for k, v in args[0].items():
                        self.addData(v, align=align)
                elif isinstance(args[0], list):
                    self._setTableWidgetRow(args, align=align)
                else:
                    if isinstance(args[0], QTableWidgetItem):
                        key = args[0].text()
                        align = args[0].textAlignment()
                    else:
                        key = args[0]
                    items = '' if duplicated_enabled else self.findItems(key, Qt.MatchFixedString)
                    if not items:
                        self._setTableWidgetRow(args, align=align)
                    else:
                        if ifExistsFunc:
                            ifExistsFunc()
                        else:
                            pass
        except Exception as e:
            print(e)
            print(sys.exc_info()[2].tb_lineno)
            print(sys.exc_info())

    def _insertTableWidgetRow(self, args, r_idx=0, c_idx=0, align=Qt.AlignVCenter):
        if len(args) == 1:
            self._setTableWidgetItem(args[0], r_idx, c_idx, align=align)
        else:
            for c in range(c_idx, len(args)+c_idx):
                args_idx = c-c_idx
                self._setTableWidgetItem(args[args_idx], r_idx, c, align=align)

    def _setTableWidgetRow(self, args, align=Qt.AlignVCenter):
        row_cnt = self.rowCount()
        self.setRowCount(row_cnt + 1)
        for i in range(len(args)):
            self._setTableWidgetItem(args[i], row_cnt, i, align=align)

    def _setTableWidgetItem(self, arg, row_cnt, column_cnt, align=Qt.AlignVCenter):
        if isinstance(arg, QWidget):
            widget = HorizontalWidget()
            widget.add_widget(arg, align=align)
            self.setCellWidget(row_cnt, column_cnt, widget)
        else:
            if isinstance(arg, QTableWidgetItem):
                align = arg.textAlignment()
            item = QTableWidgetItem(arg)
            item.setTextAlignment(align)
            self.setItem(row_cnt, column_cnt, item)
            self.setCurrentItem(item)

    def insertData(self, datas: iter, r_idx=0, c_idx=0, align=Qt.AlignVCenter, ifExistsFunc=None, duplicated_enabled=False):
        self._insertItem(args=datas, r_idx=r_idx, c_idx=c_idx, align=align, ifExistsFunc=ifExistsFunc, duplicated_enabled=duplicated_enabled)

    def insertDatas(self, datas: iter, r_idx=0, c_idx=0, align=Qt.AlignVCenter, ifExistsFunc=None, duplicated_enabled=False, set_first_row_as_current=False):
        for data in datas:
            self.insertData(data, r_idx=r_idx, c_idx=c_idx, align=align, ifExistsFunc=ifExistsFunc, duplicated_enabled=duplicated_enabled)
            r_idx += 1
        if set_first_row_as_current:
            self.setCurrentIndex(self.model().index(0, 0))

    def addData(self, datas: iter, align=Qt.AlignVCenter, ifExistsFunc=None, duplicated_enabled=False):
        # self.setColumnCount(max(self.columnCount(), len(datas))) set the count of column dynamically
        self._setItem(args=datas, align=align, ifExistsFunc=ifExistsFunc, duplicated_enabled=duplicated_enabled)

    def addDatas(self, datas: iter, align=Qt.AlignVCenter, ifExistsFunc=None, duplicated_enabled=False, set_first_row_as_current=False):
        for data in datas:
            self.addData(data, align=align, ifExistsFunc=ifExistsFunc, duplicated_enabled=duplicated_enabled)
        if set_first_row_as_current:
            self.setCurrentIndex(self.model().index(0, 0))

    def cellWidget(self, row: int, column: int):
        widget = super().cellWidget(row, column)
        if widget:
            return widget.layout().itemAt(0).widget()

    def getAllItems(self, except_widget=True):
        all_items = []
        for i in range(self.rowCount()):
            row_item = []
            for j in range(self.columnCount()):
                item = self.item(i, j)
                if item:
                    row_item.append(self.item(i, j))
                else:
                    if except_widget:
                        pass
                    else:
                        itemWidget = self.cellWidget(i, j)
                        if itemWidget:
                            row_item.append(itemWidget)
            all_items.append(tuple(row_item))
        return all_items

    def getCountOfItems(self, except_widget=True):
        count_of_items = 0
        row_col_items = self.getAllItems(except_widget=except_widget)
        for row_items in row_col_items:
            count_of_items += len(row_items)
        return count_of_items
