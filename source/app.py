import logging
import os
import threading

from PySide6 import QtGui, QtCore

from forms.main_screen_menu import MainScreenMenu
from forms.main_window import MainWindow

ll = logging.getLogger(__name__)


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

    def attempt_close(self):
        message = "Are you sure you want to close the application?"
        self.open_message_popup('message', message, None, self.close, lambda: None)

    def close(self):
        if self.current_user:
            self.logout_user()
        if self.source_tender:
            self.source_tender.close()
        if self.live_tender:
            self.live_tender.close()
        self.close_hardware_connections()
        ll.info("app closing")
        self.close_hardware_connections()
        QtCore.QCoreApplication.quit()

    def attempt_logout(self):
        message = "Are you sure you want to logout?"
        self.open_message_popup('message', message, None, self.logout_user, lambda: None)

    def logout_user(self):
        id = self.current_user.uuid
        self.user_roles.logout_user(id)
        self.user_info_logging("is logging out")
        ll.info("User is logging out")
        self.current_user = None
        self.role = None
        self.close_recipe_utility()
        self.go_to_home_page()
        self.controller.update_current_user("")
        self.change_menu_page('Login')

    def add_main_menu(self, widget):
        self.view.add_main_menu(widget)
