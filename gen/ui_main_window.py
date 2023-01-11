# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_window.ui'
##
# Created by: Qt User Interface Compiler version 5.15.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . import resources_rc
from . import resources_rc
from . import resources_rc
from . import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 760)
        MainWindow.setStyleSheet(u"QFrame#MainWindow{\n"
                                 "background-color: qlineargradient(spread:reflect, x1:0.7, y1:0.725, x2:0.71, y2:0.735, stop:0.619318 rgba(255, 255, 255, 255), stop:0.642045 rgba(252, 252, 252, 255));\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "background-color: #eeeeee;\n"
                                 "border-style: outset;\n"
                                 "border-width: 0px;\n"
                                 "border-radius: 7px;\n"
                                 "padding: 4px;\n"
                                 "font-size:25px;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color: #dddddd;\n"
                                 "}\n"
                                 "QPushButton:pressed{\n"
                                 "background-color: #cccccc;\n"
                                 "}")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.stackedWidget_main = QStackedWidget(MainWindow)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.horizontalLayout = QHBoxLayout(self.page_main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.stackedWidget_screens = QStackedWidget(self.page_main)
        self.stackedWidget_screens.setObjectName(u"stackedWidget_screens")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_screens.sizePolicy().hasHeightForWidth())
        self.stackedWidget_screens.setSizePolicy(sizePolicy)
        self.stackedWidget_screens.setStyleSheet(u"QLabel{\n"
                                                 "font-family:\"Consolas\";\n"
                                                 "font-size:60px;\n"
                                                 "}\n"
                                                 "QPushButton{\n"
                                                 "background-color: #eeeeee;\n"
                                                 "border-style: outset;\n"
                                                 "border-width: 0px;\n"
                                                 "border-radius: 7px;\n"
                                                 "max-width: 400px;\n"
                                                 "padding: 4px;\n"
                                                 "font-size:25px;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "background-color: #dddddd;\n"
                                                 "}\n"
                                                 "QPushButton:pressed{\n"
                                                 "background-color: #cccccc;\n"
                                                 "}")

        self.horizontalLayout.addWidget(self.stackedWidget_screens)

        self.horizontalLayout.setStretch(0, 1)
        self.stackedWidget_main.addWidget(self.page_main)
        self.page_utility = QWidget()
        self.page_utility.setObjectName(u"page_utility")
        self.verticalLayout_3 = QVBoxLayout(self.page_utility)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget_main.addWidget(self.page_utility)

        self.verticalLayout.addWidget(self.stackedWidget_main)

        self.retranslateUi(MainWindow)

        self.stackedWidget_main.setCurrentIndex(0)
        self.stackedWidget_screens.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TruView", None))
    # retranslateUi
