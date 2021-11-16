# simplePyQt5

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Class Overview](#class-overview)
* [Setup](#setup)

## General Info
Being able to add a couple of Qt widgets and separator at once, align them easily, no need to make layout.

## Technologies
* PyQt5 version 5.15.6

## Setup
```
$ pip install git+https://github.com/yjg30737/simplePyQt5.git
```
Keep in mind that PyQt5 version 5.15.6 will be automatically downloaded.

## Class Overview
* HorizontalWidget
Add widgets and separators horizontally.
* VerticalWidget
Add widgets and separators vertically.
* LeftRightWidget
Add some widgets left side of the widget and add the others right side.
Unlike QFormLayout which only can set QLabel to the one side, You can add a bunch of other stuffs like QComboBox, QCheckBox.

## Usage
* HorizontalWidget
```python
    from simplePyQt5.horizontalWidget import HorizontalWidget
    ...
    horizontalWidget = HorizontalWidget()
    btn1 = QPushButton()
    btns = QPushButton()
    # Add two buttons horizontally, "''" between to buttons is separator, align parameter make widgets align
    horizontalWidget.addWidgets([btn1, '', btn2], align=Qt.AlignCenter)
```
* VerticalWidget

Same as HorizontalWidget.

* LeftRightWidget
```python
    from simplePyQt5.leftRightWidget import LeftRightWidget
    ...
    lrWidget = LeftRightWidget()
    lineEdit = QLineEdit()
    btn = QPushButton()
    lrWidget.setLeftWidgets([lineEdit]) # Add lineEdit left side of the lrWidget
    lrWidget.setRightWidgets([btn]) # Add btn right side of the lrWidget
