# simplePyQt5

## Table of Contents
* [General Info](#general-info)
* [Requirements](#requirements)
* [Class Overview](#class-overview)
* [Setup](#setup)
* [Usage](#usage)

## General Info
Being able to add a couple of Qt widgets and separator at once, align them easily, no need to make layout.
This package can come in handy to someone who want to make prototype UI quick.

## Requirements
* PyQt5

## Class Overview
* HorizontalWidget

Add widgets and separators horizontally.

* VerticalWidget

Add widgets and separators vertically.

* LeftRightWidget

Add some widgets left side of the widget and add the others right side.
Unlike QFormLayout which only can set QLabel to the one side, You can add a bunch of other stuffs like QComboBox, QCheckBox.

* TopLeftRightWidget

This module inherits LeftRightWidget.
Top of this widget is LeftRightWidget and bottom part of this you can add/set a bunch of widgets such as QListWidget or separators. 

## Setup
```
$ pip install pyqt5 # if pyqt5 is not installed in your package library
$ pip install git+https://github.com/yjg30737/simplePyQt5.git
```

## Usage
* HorizontalWidget

Code
```python
    from simplePyQt5.horizontalWidget import HorizontalWidget
    ...
    horizontalWidget = HorizontalWidget()
    btn1 = QPushButton('btn1')
    btn2 = QPushButton('btn2')
    # Add two buttons horizontally, "''" between to buttons is separator, align parameter make widgets align
    horizontalWidget.addWidgets([btn1, '', btn2], align=Qt.AlignCenter)
```
Result

![HorizontalWidget](./examples/horizontalWidgetExample.png)

* VerticalWidget

Code

Same as HorizontalWidget. Only difference is name.

Result

![VerticalWidget](./examples/verticalWidgetExample.png)

* LeftRightWidget
```python
    from simplePyQt5.leftRightWidget import LeftRightWidget
    ...
    lrWidget = LeftRightWidget()
    lineEdit = QLineEdit()
    lineEdit.setFixedWidth(80) # Prevent width of lineEdit grow endlessly to show this modules feature
    btn = QPushButton()
    lrWidget.setLeftWidgets([lineEdit]) # Add lineEdit left side of the lrWidget
    lrWidget.setRightWidgets([btn]) # Add btn right side of the lrWidget
```
Result

![LeftRightWidget](./examples/leftRightWidgetExample.png)

* TopLeftRightWidget

As i said this inherits LeftRightWidget so its usage is kinda simillar to LeftRightWidget.

Code
```python
    from simplePyQt5.topLeftRightWidget import TopLeftRightWidget
    ...
    tlrWidget = TopLeftRightWidget()
    lbl = QLabel('Files')
    addBtn = QPushButton('Add')
    delBtn = QPushButton('Delete')
    listWidget = QListWidget()
    tlrWidget.setLeftWidgets([lbl])
    tlrWidget.setRightWidgets([addBtn, delBtn])
    tlrWidget.addBottomWidget(listWidget)
    self.setCentralWidget(tlrWidget)
```
Result

![TopLeftRightWidget](./examples/topLeftRightWidgetExample.png)

* Other

These classes' content margins are set to zero as default, so if you want to set the margin then
```python
    lrWidget = LeftRightWidget()
    lay = lrWidget.layout()
    lay.setContentMargins(5, 5, 5, 5)
```
get the widget's layout like this and set content margins or anything such as spacing.
