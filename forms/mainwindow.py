# from PySide6.QtCore import QSize
# from PySide6.QtGui import QAction, QIcon
# from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QHBoxLayout, QVBoxLayout,
# QGraphicsScene, QLineEdit, QLabel

# from apis import spotipy_audio_features_for_track


# class MainWindow(QMainWindow):
#     def __init__(self, app):
#         super().__init__()
#         self.app = app  # declare an app member
#         self.setWindowTitle("Spotify Audio Features")

#         # MenuBar and menus
#         # menu_bar = self.menuBar()
#         # file_menu = menu_bar.addMenu("File")
#         # quit_action = file_menu.addAction("Quit")
#         # quit_action.triggered.connect(self.quit_app)

#         # edit_menu = menu_bar.addMenu("Edit")
#         # edit_menu.addAction("Copy")
#         # edit_menu.addAction("Cut")
#         # edit_menu.addAction("Paste")
#         # edit_menu.addAction("Undo")
#         # edit_menu.addAction("Redo")

#         # A bunch of other menu options just for the fun of it
#         # menu_bar.addMenu("Window")
#         # menu_bar.addMenu("Setting")
#         # menu_bar.addMenu("Help")

#         # Working with toolbars
#         # toolbar = QToolBar("My main toolbar")
#         # toolbar.setIconSize(QSize(16, 16))
#         # self.addToolBar(toolbar)

#         # Add the quit action to the toolbar
#         # toolbar.addAction(quit_action)

#         # action1 = QAction("Get Whole Album Features", self)
#         # action1.setStatusTip("Use the Spotify API to get the album features for A Beautiful Letdown")
#         # action1.triggered.connect(lambda: self.toolbar_button_click(
#         #     spotipy_audio_features_for_track.get_whole_album_features))
#         # toolbar.addAction(action1)

#         # action2 = QAction(QIcon("start.png"), "Get Track Features", self)
#         # action2.setStatusTip("Getting Track Features")
#         # action2.triggered.connect(lambda: self.toolbar_button_click(self.get_track_features))
#         # # action2.setCheckable(True)
#         # toolbar.addAction(action2)

#         # toolbar.addSeparator()
#         # toolbar.addWidget(QPushButton("Click here"))

#         # Working with status bars
#         # self.setStatusBar(QStatusBar(self))

#         # A set of signals we can connect to
#         label = QLabel("Track Name : ")
#         self.line_edit = QLineEdit()
#         self.line_edit.returnPressed.connect(self.return_pressed)
#         self.line_edit.textEdited.connect(self.text_edited)

#         button_get_track_features = QPushButton("Get Audio Features")
#         button_get_track_features.setToolTip("Audio Features for Fire on The Cathedral by Sun Theater")
#         button_get_track_features.clicked.connect(self.get_track_features)

#         button = QPushButton("Grab data")
#         button.clicked.connect(self.button_clicked)
#         self.text_holder_label = QLabel("I AM HERE")

#         h_layout = QHBoxLayout()
#         h_layout.addWidget(label)
#         h_layout.addWidget(self.line_edit)

#         v_layout = QVBoxLayout()
#         v_layout.addLayout(h_layout)
#         v_layout.addWidget(button)
#         v_layout.addWidget(self.text_holder_label)

#         self.setLayout(v_layout)

#     def get_track_features(self):
#         spotipy_audio_features_for_track.get_fire_on_the_cathedral_features()

#     def quit_app(self):
#         self.app.quit()

#     def toolbar_button_click(self, func):
#         func()
#         self.statusBar().showMessage("Message from my app", 3000)

#     # Line Edit/Label Slots
#     def button_clicked(self):
#         #print("Fullname : ",self.line_edit.text())
#         self.text_holder_label.setText(self.line_edit.text())

#     def text_changed(self):
#         print("Text  changed to ", self.line_edit.text())
#         self.text_holder_label.setText(self.line_edit.text())

#     def cursor_position_changed(self, old, new):
#         print("cursor old position : ", old, " -new position : ", new)

#     def editing_finished(self):
#         print("Editing finished")

#     def return_pressed(self):
#         print("Return pressed")

#     def selection_changed(self):
#         print("Selection Changed : ", self.line_edit.selectedText())

#     def text_edited(self, new_text):
#         print("Text edited. New text : ", new_text)


# if __name__ == "__main__":
#     from PySide6.QtWidgets import QApplication
#     from forms.mainwindow import MainWindow
#     import sys

#     app = QApplication(sys.argv)

#     window = MainWindow(app)
#     window.show()

#     app.exec()

from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel and QLineEdit")

        # A set of signals we can connect to
        label = QLabel("Fullname : ")
        self.line_edit = QLineEdit()
        # self.line_edit.textChanged.connect(self.text_changed)
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        # self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.returnPressed.connect(self.return_pressed)
        # self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        button = QPushButton("Grab data")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel("I AM HERE")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)

    # Slots
    def button_clicked(self):
        #print("Fullname : ",self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())

    def text_changed(self):
        print("Text  changed to ", self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())

    def cursor_position_changed(self, old, new):
        print("cursor old position : ", old, " -new position : ", new)

    def editing_finished(self):
        print("Editing finished")

    def return_pressed(self):
        print("Return pressed")

    def selection_changed(self):
        print("Selection Changed : ", self.line_edit.selectedText())

    def text_edited(self, new_text):
        print("Text edited. New text : ", new_text)
