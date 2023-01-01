# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_screen_menu.ui'
##
# Created by: Qt User Interface Compiler version 5.15.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainScreenMenu(object):
    def setupUi(self, MainScreenMenu):
        if not MainScreenMenu.objectName():
            MainScreenMenu.setObjectName(u"MainScreenMenu")
        MainScreenMenu.resize(319, 668)
        MainScreenMenu.setStyleSheet(u"#widget_menu{\n"
                                     "background-color: qradialgradient(spread:pad,cx: 0.5, cy: 0.5, radius: 2.3, fx: 0.5, fy: 0.5, stop:0.1 rgba(230, 230, 230, 150), stop:0.3 rgba(200,200,200, 150), stop:0.35 rgba(230,230,230, 150));\n"
                                     "border-radius:10px;\n"
                                     "}\n"
                                     "QStackedWidget{\n"
                                     "background-color: transparent;\n"
                                     "}\n"
                                     "QLabel{\n"
                                     "font-family:\"Consolas\";\n"
                                     "font-size:30px;\n"
                                     "}\n"
                                     "QPushButton{\n"
                                     "background-color: #ffffff;\n"
                                     "border-style: outset;\n"
                                     "border-width: 0px;\n"
                                     "border-radius: 7px;\n"
                                     "padding: 4px;\n"
                                     "font-size:25px;\n"
                                     "font-family:\"Consolas\";\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: #dddddd;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "background-color: qradialgradient(spread:pad,cx: 0.5, cy: 0.5, radius: 2, fx: 0.5, fy: 0.5, stop:0.1 rgba(193, 222, 245, 255), stop:0.4 rgba(107, 148, 181, 255), stop:0.45 rgba(193, 222, 245, 255));\n"
                                     "}\n"
                                     "QPushButton:checked{\n"
                                     "background-color: qradialgradient(spread:pad,cx: 0.5, cy: 0.5, radius: 2, fx: 0.5, fy: 0.5, stop:0.1 rgba(193, 222, 245, 255), stop:0"
                                     ".4 rgba(107, 148, 181, 255), stop:0.45 rgba(193, 222, 245, 255));\n"
                                     "}")
        self.verticalLayout_3 = QVBoxLayout(MainScreenMenu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_menu = QWidget(MainScreenMenu)
        self.widget_menu.setObjectName(u"widget_menu")
        self.widget_menu.setMinimumSize(QSize(0, 650))
        self.widget_menu.setMaximumSize(QSize(16777215, 650))
        self.verticalLayout_6 = QVBoxLayout(self.widget_menu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_menu = QStackedWidget(self.widget_menu)
        self.stackedWidget_menu.setObjectName(u"stackedWidget_menu")
        self.stackedWidget_menu.setMinimumSize(QSize(300, 600))
        self.stackedWidget_menu.setMaximumSize(QSize(300, 600))
        self.stackedWidget_menu.setStyleSheet(u"")
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.verticalLayout_2 = QVBoxLayout(self.page_login)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.label_login = QLabel(self.page_login)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setStyleSheet(u"background-color:rgba(0,0,0,0);")
        self.label_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_login)

        self.pushButton_login = QPushButton(self.page_login)
        self.pushButton_login.setObjectName(u"pushButton_login")
        font = QFont()
        font.setFamily(u"Consolas")
        self.pushButton_login.setFont(font)
        self.pushButton_login.setFocusPolicy(Qt.NoFocus)
        self.pushButton_login.setFlat(False)

        self.verticalLayout_2.addWidget(self.pushButton_login)

        self.verticalSpacer_5 = QSpacerItem(20, 387, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.pushButton_login_back = QPushButton(self.page_login)
        self.pushButton_login_back.setObjectName(u"pushButton_login_back")
        self.pushButton_login_back.setFont(font)
        self.pushButton_login_back.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_2.addWidget(self.pushButton_login_back)

        self.stackedWidget_menu.addWidget(self.page_login)
        self.page_main_menu = QWidget()
        self.page_main_menu.setObjectName(u"page_main_menu")
        self.verticalLayout_4 = QVBoxLayout(self.page_main_menu)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.label_main = QLabel(self.page_main_menu)
        self.label_main.setObjectName(u"label_main")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_main.sizePolicy().hasHeightForWidth())
        self.label_main.setSizePolicy(sizePolicy)
        self.label_main.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_main)

        self.pushButton_recipe_menu = QPushButton(self.page_main_menu)
        self.pushButton_recipe_menu.setObjectName(u"pushButton_recipe_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_recipe_menu.sizePolicy().hasHeightForWidth())
        self.pushButton_recipe_menu.setSizePolicy(sizePolicy1)
        self.pushButton_recipe_menu.setMinimumSize(QSize(0, 40))
        self.pushButton_recipe_menu.setFont(font)
        self.pushButton_recipe_menu.setFocusPolicy(Qt.NoFocus)
        self.pushButton_recipe_menu.setFlat(False)

        self.verticalLayout_4.addWidget(self.pushButton_recipe_menu)

        self.pushButton_tools = QPushButton(self.page_main_menu)
        self.pushButton_tools.setObjectName(u"pushButton_tools")
        self.pushButton_tools.setMinimumSize(QSize(0, 40))
        self.pushButton_tools.setFont(font)
        self.pushButton_tools.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_4.addWidget(self.pushButton_tools)

        self.pushButton_settings = QPushButton(self.page_main_menu)
        self.pushButton_settings.setObjectName(u"pushButton_settings")

        self.verticalLayout_4.addWidget(self.pushButton_settings)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButton_logout = QPushButton(self.page_main_menu)
        self.pushButton_logout.setObjectName(u"pushButton_logout")
        self.pushButton_logout.setFont(font)
        self.pushButton_logout.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_4.addWidget(self.pushButton_logout)

        self.stackedWidget_menu.addWidget(self.page_main_menu)
        self.page_recipes = QWidget()
        self.page_recipes.setObjectName(u"page_recipes")
        self.verticalLayout_5 = QVBoxLayout(self.page_recipes)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.label_recipe = QLabel(self.page_recipes)
        self.label_recipe.setObjectName(u"label_recipe")
        sizePolicy.setHeightForWidth(self.label_recipe.sizePolicy().hasHeightForWidth())
        self.label_recipe.setSizePolicy(sizePolicy)
        self.label_recipe.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_recipe)

        self.pushButton_add_recipe = QPushButton(self.page_recipes)
        self.pushButton_add_recipe.setObjectName(u"pushButton_add_recipe")
        self.pushButton_add_recipe.setEnabled(False)
        self.pushButton_add_recipe.setMinimumSize(QSize(0, 40))
        self.pushButton_add_recipe.setFont(font)
        self.pushButton_add_recipe.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_5.addWidget(self.pushButton_add_recipe)

        self.pushButton_recipe_settings = QPushButton(self.page_recipes)
        self.pushButton_recipe_settings.setObjectName(u"pushButton_recipe_settings")
        self.pushButton_recipe_settings.setFont(font)
        self.pushButton_recipe_settings.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_5.addWidget(self.pushButton_recipe_settings)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.pushButton_recipe_back = QPushButton(self.page_recipes)
        self.pushButton_recipe_back.setObjectName(u"pushButton_recipe_back")
        self.pushButton_recipe_back.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_5.addWidget(self.pushButton_recipe_back)

        self.stackedWidget_menu.addWidget(self.page_recipes)
        self.page_tools = QWidget()
        self.page_tools.setObjectName(u"page_tools")
        self.verticalLayout = QVBoxLayout(self.page_tools)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.label_tools = QLabel(self.page_tools)
        self.label_tools.setObjectName(u"label_tools")
        sizePolicy.setHeightForWidth(self.label_tools.sizePolicy().hasHeightForWidth())
        self.label_tools.setSizePolicy(sizePolicy)
        self.label_tools.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_tools)

        self.pushButton_warmup = QPushButton(self.page_tools)
        self.pushButton_warmup.setObjectName(u"pushButton_warmup")
        self.pushButton_warmup.setMinimumSize(QSize(0, 40))
        self.pushButton_warmup.setFont(font)
        self.pushButton_warmup.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.pushButton_warmup)

        self.pushButton_manual_controls = QPushButton(self.page_tools)
        self.pushButton_manual_controls.setObjectName(u"pushButton_manual_controls")

        self.verticalLayout.addWidget(self.pushButton_manual_controls)

        self.pushButton_live_view = QPushButton(self.page_tools)
        self.pushButton_live_view.setObjectName(u"pushButton_live_view")
        self.pushButton_live_view.setEnabled(True)
        self.pushButton_live_view.setFont(font)
        self.pushButton_live_view.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.pushButton_live_view)

        self.pushButton_calibrate = QPushButton(self.page_tools)
        self.pushButton_calibrate.setObjectName(u"pushButton_calibrate")
        self.pushButton_calibrate.setFont(font)
        self.pushButton_calibrate.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.pushButton_calibrate)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pushButton_tools_back = QPushButton(self.page_tools)
        self.pushButton_tools_back.setObjectName(u"pushButton_tools_back")
        self.pushButton_tools_back.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.pushButton_tools_back)

        self.stackedWidget_menu.addWidget(self.page_tools)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_7 = QVBoxLayout(self.page_settings)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.label_settings = QLabel(self.page_settings)
        self.label_settings.setObjectName(u"label_settings")
        self.label_settings.setStyleSheet(u"background-color:rgba(0,0,0,0);")
        self.label_settings.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_settings)

        self.pushButton_hardware_settings = QPushButton(self.page_settings)
        self.pushButton_hardware_settings.setObjectName(u"pushButton_hardware_settings")
        self.pushButton_hardware_settings.setFont(font)
        self.pushButton_hardware_settings.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_7.addWidget(self.pushButton_hardware_settings)

        self.pushButton_preferences = QPushButton(self.page_settings)
        self.pushButton_preferences.setObjectName(u"pushButton_preferences")
        self.pushButton_preferences.setMinimumSize(QSize(0, 40))
        self.pushButton_preferences.setFont(font)
        self.pushButton_preferences.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_7.addWidget(self.pushButton_preferences)

        self.pushButton_user_settings = QPushButton(self.page_settings)
        self.pushButton_user_settings.setObjectName(u"pushButton_user_settings")
        self.pushButton_user_settings.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_7.addWidget(self.pushButton_user_settings)

        self.pushButton_permissions = QPushButton(self.page_settings)
        self.pushButton_permissions.setObjectName(u"pushButton_permissions")

        self.verticalLayout_7.addWidget(self.pushButton_permissions)

        self.pushButton_about = QPushButton(self.page_settings)
        self.pushButton_about.setObjectName(u"pushButton_about")

        self.verticalLayout_7.addWidget(self.pushButton_about)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.pushButton_settings_back = QPushButton(self.page_settings)
        self.pushButton_settings_back.setObjectName(u"pushButton_settings_back")
        self.pushButton_settings_back.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_7.addWidget(self.pushButton_settings_back)

        self.stackedWidget_menu.addWidget(self.page_settings)

        self.verticalLayout_6.addWidget(self.stackedWidget_menu)

        self.widget = QWidget(self.widget_menu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.pushButton_exit = QPushButton(self.widget)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setMinimumSize(QSize(0, 0))
        self.pushButton_exit.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.pushButton_exit)

        self.verticalLayout_6.addWidget(self.widget)

        self.verticalLayout_3.addWidget(self.widget_menu)

        self.retranslateUi(MainScreenMenu)

        self.stackedWidget_menu.setCurrentIndex(3)

        QMetaObject.connectSlotsByName(MainScreenMenu)
    # setupUi

    def retranslateUi(self, MainScreenMenu):
        MainScreenMenu.setWindowTitle(QCoreApplication.translate("MainScreenMenu", u"Form", None))
        self.label_login.setText(QCoreApplication.translate("MainScreenMenu", u"Login", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainScreenMenu", u"Select User", None))
        self.pushButton_login_back.setText(QCoreApplication.translate("MainScreenMenu", u"Back", None))
        self.label_main.setText(QCoreApplication.translate("MainScreenMenu", u"Main", None))
        self.pushButton_recipe_menu.setText(QCoreApplication.translate("MainScreenMenu", u"Recipes", None))
        self.pushButton_tools.setText(QCoreApplication.translate("MainScreenMenu", u"Tools", None))
        self.pushButton_settings.setText(QCoreApplication.translate("MainScreenMenu", u"Settings", None))
        self.pushButton_logout.setText(QCoreApplication.translate("MainScreenMenu", u"Logout", None))
        self.label_recipe.setText(QCoreApplication.translate("MainScreenMenu", u"Recipes", None))
        self.pushButton_add_recipe.setText(QCoreApplication.translate("MainScreenMenu", u"Add Recipe", None))
        self.pushButton_recipe_settings.setText(QCoreApplication.translate("MainScreenMenu", u"Recipe Settings", None))
        self.pushButton_recipe_back.setText(QCoreApplication.translate("MainScreenMenu", u"Back", None))
        self.label_tools.setText(QCoreApplication.translate("MainScreenMenu", u"Tools", None))
        self.pushButton_warmup.setText(QCoreApplication.translate("MainScreenMenu", u"Warmup Source", None))
        self.pushButton_manual_controls.setText(QCoreApplication.translate("MainScreenMenu", u"Manual Controls", None))
        self.pushButton_live_view.setText(QCoreApplication.translate("MainScreenMenu", u"Live View", None))
        self.pushButton_calibrate.setText(QCoreApplication.translate("MainScreenMenu", u"Calibrate Camera", None))
        self.pushButton_tools_back.setText(QCoreApplication.translate("MainScreenMenu", u"Back", None))
        self.label_settings.setText(QCoreApplication.translate("MainScreenMenu", u"Settings", None))
        self.pushButton_hardware_settings.setText(
            QCoreApplication.translate("MainScreenMenu", u" Hardware Settings", None))
        self.pushButton_preferences.setText(QCoreApplication.translate("MainScreenMenu", u"Preferences", None))
        self.pushButton_user_settings.setText(QCoreApplication.translate("MainScreenMenu", u"User Settings", None))
        self.pushButton_permissions.setText(QCoreApplication.translate("MainScreenMenu", u"User Permissions", None))
        self.pushButton_about.setText(QCoreApplication.translate("MainScreenMenu", u"About", None))
        self.pushButton_settings_back.setText(QCoreApplication.translate("MainScreenMenu", u"Back", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainScreenMenu", u"Exit To Desktop", None))
    # retranslateUi
