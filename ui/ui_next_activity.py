# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-next-activity.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(290, 125)
        Form.setMinimumSize(QSize(0, 100))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.next_subtitle = QLabel(Form)
        self.next_subtitle.setObjectName(u"next_subtitle")
        self.next_subtitle.setGeometry(QRect(40, 20, 211, 31))
        font = QFont()
        font.setFamily(u"Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.next_subtitle.setFont(font)
        self.next_subtitle.setStyleSheet(u"color: rgba(0, 0, 0, 90);\n"
"font-weight: bold;")
        self.next_subtitle.setTextFormat(Qt.PlainText)
        self.next_subtitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.next_lesson_text = QLabel(Form)
        self.next_lesson_text.setObjectName(u"next_lesson_text")
        self.next_lesson_text.setGeometry(QRect(40, 40, 211, 51))
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei")
        font1.setPointSize(21)
        font1.setBold(True)
        font1.setWeight(75)
        self.next_lesson_text.setFont(font1)
        self.next_lesson_text.setStyleSheet(u"border: none;\n"
"color: rgba(37, 37, 37, 255);\n"
"font-weight: bold")
        self.next_lesson_text.setTextFormat(Qt.PlainText)
        self.next_lesson_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 271, 91))
        self.label.setStyleSheet(u"background-color: rgba(242, 243, 245, 242);\n"
"border-radius: 8px")
        self.label.raise_()
        self.next_subtitle.raise_()
        self.next_lesson_text.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.next_subtitle.setText(QCoreApplication.translate("Form", u"\u63a5\u4e0b\u6765", None))
        self.next_lesson_text.setText(QCoreApplication.translate("Form", u"\u6d4b\u8bd5\u6d4b\u8bd5", None))
        self.label.setText("")
    # retranslateUi

