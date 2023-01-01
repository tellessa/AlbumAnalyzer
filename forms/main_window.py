from PySide6 import QtGui, QtCore, QtWidgets

from gen.ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QFrame):

    def __init__(self, app, qApp):
        super(MainWindow, self).__init__()
        self.app = app
        self.qApp = qApp
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._configure()
        self.place()
        app_icon = QtGui.QIcon()
        app_icon.addPixmap(QtGui.QPixmap(":/assets/creative/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(app_icon)

    def closeEvent(self, event: QtGui.QCloseEvent):
        self.app.attempt_close()
        event.ignore()

    def _configure(self):
        self.ui.stackedWidget_main.setCurrentIndex(0)
        self.ui.stackedWidget_screens.setCurrentIndex(0)

    def add_controller(self, control):
        lyt = self.ui.verticalLayout.layout()
        lyt.insertWidget(2, control)

    def add_main_menu(self, widget):
        lyt = self.ui.page_main.layout()
        lyt.insertWidget(0, widget, 0)

    def add_utility(self, widget):
        lyt = self.ui.page_utility.layout()
        lyt.insertWidget(0, widget)

    def add_page(self, widget):
        self.ui.stackedWidget_screens.addWidget(widget)

    def remove_page(self, widget):
        self.ui.stackedWidget_screens.removeWidget(widget)

    def change_utility(self, index):
        self.ui.stackedWidget_main.setCurrentIndex(index)

    def change_page(self, widget, back: bool):
        if back:
            index = self.ui.stackedWidget_screens.currentIndex()
            index -= 1
        else:
            index = self.ui.stackedWidget_screens.indexOf(widget)
        self.ui.stackedWidget_screens.setCurrentIndex(index)

    def go_to_home_page(self):
        self.ui.stackedWidget_screens.setCurrentIndex(0)

    def choose_user(self, _: bool):
        self.ui.stackedWidget_login.setCurrentIndex(1)

    def place(self):
        qtSettings = QtCore.QSettings()

        # Set main screen location
        if qtSettings.contains("ui/main screen"):
            screen_name = qtSettings.value("ui/main screen")
        else:
            screen_name = ""

        screens = QtGui.QGuiApplication.screens()
        for screen in screens:
            if screen.name() == screen_name:
                break
        else:
            screen = screens[0]

        self.setGeometry(screen.availableGeometry())
