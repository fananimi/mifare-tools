import sys
import signal
from PySide2 import QtCore, QtGui, QtWidgets
from ui.main import Ui_MainWindow


class MifareTools(Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MifareTools, self).__init__(parent)
        self.setupUi(self)
        self._register_signal()

    # --------------------------------------------------------------------------------
    # ****************** All signals must register on this section ******************|
    # --------------------------------------------------------------------------------
    def _register_signal(self):
        self.btnReloadReader.clicked.connect(self.on_click_button)
        self.btnConnetPICC.clicked.connect(self.on_click_button)
        self.btnAuthKeyA.clicked.connect(self.on_click_button)
        self.btnAuthKeyB.clicked.connect(self.on_click_button)
        self.btnFactoryKeyA.clicked.connect(self.on_click_button)
        self.btnFactoryKeyB.clicked.connect(self.on_click_button)

    def on_click_button(self):
        btnID = self.sender().objectName()
        if btnID == 'btnReloadReader':
            print("btnReloadReader")
            return
        elif btnID == "btnConnetPICC":
            print("btnConnetPICC")
            return
        elif btnID == "btnReloadReader":
            print("btnReloadReader")
            return
        elif btnID == "btnAuthKeyA":
            print("btnAuthKeyA")
            return
        elif btnID == "btnAuthKeyB":
            print("btnAuthKeyB")
            return
        elif btnID == "btnFactoryKeyA":
            print("btnFactoryKeyA")
            return
        elif btnID == "btnFactoryKeyB":
            print("btnFactoryKeyB")
            return


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtWidgets.QApplication(sys.argv)

    # ui main
    window = MifareTools()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

