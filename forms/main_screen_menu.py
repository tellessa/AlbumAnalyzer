from PySide6 import QtWidgets
from typing import TYPE_CHECKING

from gen.ui_main_screen_menu import Ui_MainScreenMenu

if TYPE_CHECKING:
    from source.app import App

import logging
ll = logging.getLogger(__name__)


class MainScreenMenu(QtWidgets.QWidget):

    MENU_ENUM = {
        'Login': 0,
        'Main': 1,
        'Recipes': 2,
        'Tools': 3,
        'Settings': 4,
    }

    def __init__(self, app: 'App'):
        super(MainScreenMenu, self).__init__()
        self.app = app
        self.ui = Ui_MainScreenMenu()
        self.ui.setupUi(self)
        self._configure()
        self.setup_connections()
        self.place()
        self.previous_btn = None
        self.previous_utility = None

    def setup_connections(self):
        self.ui.pushButton_exit.clicked.connect(self.app.attempt_close)

        # Login Menu
        self.ui.pushButton_login.clicked.connect(lambda: self.check_back_visible(True))
        self.ui.pushButton_login_back.clicked.connect(lambda: self.check_back_visible(False))
        self.ui.pushButton_logout.clicked.connect(self.app.attempt_logout)

        # Recipe Menu
        self.ui.pushButton_recipe_menu.clicked.connect(lambda: self.app.open_recipe_page(True))
        self.ui.pushButton_recipe_back.clicked.connect(lambda: self.back(True))
        self.ui.pushButton_recipe_settings.clicked.connect(lambda: self.app.open_popup('global recipe popup'))

        # Tools Menu
        self.ui.pushButton_tools.clicked.connect(lambda: self.change_menu_page('Tools', True))
        self.ui.pushButton_tools_back.clicked.connect(lambda: self.back(True))

        # Settings Menu
        self.ui.pushButton_settings.clicked.connect(lambda: self.change_menu_page("Settings", True))
        self.ui.pushButton_settings_back.clicked.connect(lambda: self.back(True))
        self.ui.pushButton_preferences.clicked.connect(lambda: self.app.open_popup('preferences popup'))
        self.ui.pushButton_hardware_settings.clicked.connect(lambda: self.app.open_popup('hardware popup'))
        self.ui.pushButton_user_settings.clicked.connect(lambda: self.app.open_user_utility('user utility'))
        self.ui.pushButton_permissions.clicked.connect(lambda: self.app.open_popup('permissions popup'))
        self.ui.pushButton_about.clicked.connect(lambda: self.app.open_popup('about popup'))

    def _configure(self):
        self.ui.stackedWidget_menu.setCurrentIndex(0)
        self.ui.pushButton_login_back.setVisible(False)

    def place(self):
        self.app.add_main_menu(self)

    def back(self, menu_back=False):
        if menu_back:
            self.app.close_pages()
            self.app.user_info_logging("selectd back button")
            ll.info("User selected back button")

    def warmup_visible(self, visible):
        self.ui.pushButton_warmup.setVisible(visible)

    def change_utility(self, index):
        self.app.change_utility(index)

    def change_menu_page(self, menu_name, user_action=False):
        # Logging user actions and automatic actions
        if user_action:
            self.app.user_info_logging(f"changed menu page to {menu_name}")
            ll.info(f"User changed menu page to {menu_name}")

        self.ui.stackedWidget_menu.setCurrentIndex(self.MENU_ENUM[menu_name])

    def hide_logout_button(self, visible):
        self.ui.pushButton_logout.setVisible(visible)

    def check_back_visible(self, visible):
        if visible:
            self.app.open_user_utility('login utility')
            # self.app.check_service_visibility()
        else:
            self.app.close_user_utility('login utility')
        self.ui.pushButton_login_back.setVisible(visible)

    def update_permissions(self, user, permissions):
        self._user = user
        visible = False
        self.ui.pushButton_hardware_settings.setVisible(False)
        if user.role in ['Administrator', "Service"]:
            visible = True
        if user.role == "Service":
            self.ui.pushButton_hardware_settings.setVisible(True)
        self.update_tools_menu(permissions, visible)
        self.update_recipe_menu(permissions)

    def update_tools_menu(self, permissions, visible):
        live = permissions['live_view']
        manual = permissions['manual_controls']
        calibration = permissions['calibration']
        tools = not all(item is False for item in [live, manual, calibration])
        self.ui.pushButton_tools.setVisible(tools)
        self.ui.pushButton_live_view.setVisible(live)
        self.ui.pushButton_manual_controls.setVisible(manual)
        self.ui.pushButton_calibrate.setVisible(calibration)
        self.ui.pushButton_permissions.setVisible(visible)
        self.ui.pushButton_preferences.setVisible(visible)
        self.ui.pushButton_preferences.setVisible(permissions['preferences_settings'])

    def update_recipe_menu(self, permissions):
        self.ui.pushButton_add_recipe.setVisible(permissions['create_recipe'])
        self.ui.pushButton_recipe_settings.setVisible(permissions['edit_global_recipe_settings'])

    def toggle_utility_buttons(self, enabled):
        self.ui.pushButton_live_view.setEnabled(enabled)
        self.ui.pushButton_calibrate.setEnabled(enabled)
