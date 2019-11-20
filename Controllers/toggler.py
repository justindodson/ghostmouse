import pyautogui

from PyQt5 import QtWidgets
import sys
from Views.MainView import Ui_MainWindow


class Toggler:

    def __init__(self):
        # variables
        self.isRunning = False

        # setup window from the Qt generated Ui_MainWindow class
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()

        # create class instance variable to reference the ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(window)

        # signal methods
        self.triggerEnableButton()

        # show window and execute application
        window.show()
        sys.exit(app.exec_())

    def triggerEnableButton(self):
        self.ui.enablebutton.clicked.connect(self.toggle_mouse)


    def toggleEnableButton(self):
        if self.isRunning:
            self.ui.enablebutton.setText('Stop')
            self.ui.enablebutton.repaint()
            self.ui.quit.setEnabled(False)
            self.control_mouse()
        else:
            self.ui.enablebutton.setText('Start')
            self.ui.enablebutton.repaint()
            self.ui.quit.setEnabled(True)
            self.ui.quit.repaint()


    def toggle_mouse(self):
        self.isRunning = not self.isRunning
        self.toggleEnableButton()

    def control_mouse(self):
        while self.isRunning:
            QtWidgets.QApplication.processEvents()
            pyautogui.moveRel(0.5, 0, duration=0.25)
            pyautogui.moveRel(-0.5, 0, duration=0.25)
