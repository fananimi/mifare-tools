import sys
import signal
from smartcard.Exceptions import NoCardException
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

    def _connect(self):
        try:
            reader_idx = self.cmbReader.currentIndex()
            reader_obj = self.reader_model.item(reader_idx)
            if not hasattr(reader_obj, 'data'):
                raise IndexError()
            self.current_connection = readers()[reader_idx].createConnection()
            self.current_connection.connect()
        except IndexError:
            self.write_statusbar("Invalid reader", "red")
        except NoCardException as e:
            self.write_statusbar(str(e), "red")
        else:
            data, sw1, sw2 = self.current_connection.transmit(toBytes("FF CA 00 00 00"))
            self.txtUID.setText(toHexString(data))
            self.txtATR.setText(toHexString(self.current_connection.getATR()))
            self.write_statusbar("OK")


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtWidgets.QApplication(sys.argv)

    # ui main
    window = MifareTools()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

