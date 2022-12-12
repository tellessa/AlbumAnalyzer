if __name__ == "__main__":
    import faulthandler
    faulthandler.enable()
    # Start logging
    import logging
    import logging.handlers
    import os.path

    # For screen capture
    import multiprocessing as mp
    # This will prevent the creation of a whole new instance of the application
    mp.freeze_support()

    ll = logging.getLogger()
    ll.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)-8s %(name)-25s %(message)s')

    # Log unhandled errors
    import sys
    import traceback
    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, tb):
        ll.error("Type " + str(exctype) + "\nValue " + str(value) +
                 "\n" + ''.join(traceback.format_tb(tb)))
        sys._excepthook(exctype, value, traceback)
    sys.excepthook = exception_hook

    # Load Qt base
    from PySide2 import QtWidgets, QtGui, QtCore

    # Application wide settings
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

    qApp = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create("Fusion"))

    # Initalize Splash
    from gen import resources_rc
    pixmap = QtGui.QPixmap(":/assets/creative/splash.svg")
    splash = QtWidgets.QSplashScreen(pixmap)
    splash.show()

    # Create App
    from source.app import App
    app = App(qApp)

    qApp.lastWindowClosed.connect(lambda: app.close())
    splash.finish(app.view)

    # Hand over control to Qt
    sys.exit(qApp.exec_())
