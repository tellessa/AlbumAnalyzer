from PySide6.QtWidgets import QApplication
# from forms.mainwindow import MainWindow
from forms.mainwindow import Widget as MainWindow
import sys

app = QApplication(sys.argv)

# window = MainWindow(app)
window = MainWindow()
window.show()

app.exec()
