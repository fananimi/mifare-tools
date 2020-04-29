import sys
import signal
import command
from smartcard.Exceptions import NoCardException, CardConnectionException
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
        self.current_connection = None
        self.reader_model = QtGui.QStandardItemModel()

        # finally we render the user interface
        self._init_ui()

    def on_click_button(self):
        btnID = self.sender().objectName()
        if btnID == 'btnReloadReader':
            self._reload_readers()
            return
        elif btnID == "btnConnetPICC":
            self._connect()
            return
        elif btnID == "btnAuthKeyA":
            return
        elif btnID == "btnAuthKeyB":
            print("btnAuthKeyB")
            return
        elif btnID == "btnFactoryKeyA":
            for i in range(0, 6):
                getattr(self, 'txtKeyA%d' % i).setText("FF")
            return
        elif btnID == "btnFactoryKeyB":
            for i in range(0, 6):
                getattr(self, 'txtKeyB%d' % i).setText("FF")
            return

    def write_statusbar(self, message, color='green'):
        self.statusbar.setStyleSheet("color: %s;" % color)
        self.statusbar.showMessage(message)

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

    def _reload_readers(self):
        self.cmbReader.clear()
        for reader in readers():
            reader_item = QtGui.QStandardItem(reader.name)
            reader_item.setData(reader)
            self.reader_model.appendRow(reader_item)

    def _get_active_reader(self):
        reader_idx = self.cmbReader.currentIndex()
        reader_obj = self.reader_model.item(reader_idx)
        if not hasattr(reader_obj, 'data'):
            return None
        return reader_obj.data()

    def _connect(self):
        try:
            reader = self._get_active_reader()
            if not reader:
                self.current_connection = None
                self.write_statusbar("No reader selected", "red")
                return

            self.current_connection = reader.createConnection()
            self.current_connection.connect()
            # get UID and ATR
            uid = self.transmit(command.UID)
            self.txtUID.setText(toHexString(uid))
            self.txtATR.setText(toHexString(self.current_connection.getATR()))
        except (NoCardException, CardConnectionException) as e:
            self._reload_readers()
            self.write_statusbar(str(e), "red")

    def transmit(self, cmd):
        reader = self._get_active_reader()
        if not reader:
            self.current_connection = None
            return
        if not self.current_connection:
            self._connect()

        data, sw1, sw2 = self.current_connection.transmit(toBytes(cmd))
        status_code = toHexString([sw1, sw2])

        status_color = "green" if status_code == '90 00' else "red"
        self.write_statusbar(status_code, status_color)

        return data


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtWidgets.QApplication(sys.argv)

    # ui main
    window = MifareTools()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

