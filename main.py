import sys
import signal
from smartcard.System import readers
from smartcard.util import toHexString, toBytes
from PySide2 import QtCore, QtGui, QtWidgets
from ui.main import Ui_MainWindow


class MifareTools(Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MifareTools, self).__init__(parent)
        self.setupUi(self)
        self._register_signal()

        # attribute registration
        self.reader_model = QtGui.QStandardItemModel()

        # finally we render the user interface
        self._init_ui()

    # --------------------------------------------------------------------------------
    # ********************* All functions shown to user is here *********************|
    # --------------------------------------------------------------------------------
    def _init_ui(self):
        # set combobox
        self.cmbReader.setModel(self.reader_model)
        self._reload_readers()

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
            self._reload_readers()
            return
        elif btnID == "btnConnetPICC":
            self._connect()
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

    def _reload_readers(self):
        self.cmbReader.clear()
        for reader in readers():
            reader_item = QtGui.QStandardItem(reader.name)
            reader_item.setData(reader)
            self.reader_model.appendRow(reader_item)

    def _connect(self):
        conn = readers()[0].createConnection()
        conn.connect()
        data, sw1, sw2 = conn.transmit(toBytes("FF CA 00 00 00"))
        self.txtUID.setText(toHexString(data))
        print (conn.getATR())
        self.txtATR.setText(toHexString(conn.getATR()))


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtWidgets.QApplication(sys.argv)

    # ui main
    window = MifareTools()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

