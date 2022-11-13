import logging
import os
import threading

from PySide2 import QtGui, QtCore

from forms.main_screen_menu import MainScreenMenu
from forms.main_window import MainWindow


class App(QtCore.QObject):
    signal_qtdo = QtCore.Signal(object)
    signal_qtdo_sync = QtCore.Signal(object, object, object)

    def __init__(self, qApp, lic_bypass, tv_version):
        super(App, self).__init__()
        self.qApp = qApp
        self.setup_ui()

    def setup_ui(self):
        self.view = MainWindow(self, self.qApp)
        self.main_menu = MainScreenMenu(self)
        self.view.showMaximized()
