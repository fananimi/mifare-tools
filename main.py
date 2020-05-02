import sys
import signal
import command
from smartcard.Exceptions import NoCardException, CardConnectionException
from smartcard.System import readers
from smartcard.util import toHexString, toBytes
from PySide2 import QtGui, QtWidgets
from ui.main import Ui_MainWindow


class MifareTools(Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MifareTools, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Mifare Tools")
        self.register_signal()

        # attribute registration
        self.is_picc_connect = False
        self.current_connection = None
        self.reader_model = QtGui.QStandardItemModel()

        # finally we render the user interface
        self.init_ui()

    def __del__(self):
        if self.is_picc_connect:
            self.disconnect_picc()

    # -------------------------------------------------------------------------
    # ****************** All functions shown to user is here ******************
    # -------------------------------------------------------------------------
    def init_ui(self):
        # set combobox
        self.cmbReader.setModel(self.reader_model)
        self.reload_readers()

    # -------------------------------------------------------------------------
    # *************** All signals must register on this section ***************
    # -------------------------------------------------------------------------
    def register_signal(self):
        # clicked signal
        self.btnReloadReader.clicked.connect(self.on_click)
        self.btnConnetPICC.clicked.connect(self.on_click)
        self.btnAuthKeyA.clicked.connect(self.on_click)
        self.btnAuthKeyB.clicked.connect(self.on_click)
        self.btnFactoryKeyA.clicked.connect(self.on_click)
        self.btnFactoryKeyB.clicked.connect(self.on_click)
        self.btnReadBlock.clicked.connect(self.on_click)
        self.btnWriteBlock.clicked.connect(self.on_click)
        self.cbASCII.clicked.connect(self.on_click)
        self.btnClearLog.clicked.connect(self.on_click)
        # comoBox changed index
        self.cmbReader.currentIndexChanged\
            .connect(self.on_combobox_index_changed)

    # -------------------------------------------------------------------------
    # ************************ Signal callback is here ************************
    # -------------------------------------------------------------------------
    def on_combobox_index_changed(self):
        sender = self.sender().objectName()
        if sender == self.cmbReader.objectName():
            cmb_idx = self.cmbReader.currentIndex()
            reader_obj = self.reader_model.item(cmb_idx)
            if hasattr(reader_obj, 'data'):
                self.current_connection = reader_obj.data().createConnection()
                self.groupBoxPICCC.setEnabled(True)
                self.write_statusbar("Reader connected")
            else:
                self.groupBoxPICCC.setEnabled(False)
                self.write_statusbar("Reader not connected", "blue")
            return

    def on_click(self):
        sender = self.sender().objectName()
        if sender == self.btnReloadReader.objectName():
            self.reload_readers()
        elif sender == self.btnConnetPICC.objectName():
            if not self.is_picc_connect:
                self.connect_picc()
            else:
                self.disconnect_picc()
        elif sender == self.btnAuthKeyA.objectName():
            cmd = command.LOAD_AUTH
            for i in range(0, 6):
                cmd += " %s" % getattr(self, 'txtKeyA%d' % i).text()
            # load auth
            self.transmit(cmd)
            # auth block
            sector = self.spnSector.value()
            block = self.spnBlock.value()
            cmd = command.get_block_auth_cmd(sector, block, command.KEY_TYPE_A)
            self.transmit(cmd)
        elif sender == self.btnAuthKeyB.objectName():
            cmd = command.LOAD_AUTH
            for i in range(0, 6):
                cmd += " %s" % getattr(self, 'txtKeyB%d' % i).text()
            # load auth
            self.transmit(cmd)
            # auth block
            sector = self.spnSector.value()
            block = self.spnBlock.value()
            cmd = command.get_block_auth_cmd(sector, block, command.KEY_TYPE_B)
            self.transmit(cmd)
        elif sender == self.btnFactoryKeyA.objectName():
            for i in range(0, 6):
                getattr(self, 'txtKeyA%d' % i).setText("FF")
        elif sender == self.btnFactoryKeyB.objectName():
            for i in range(0, 6):
                getattr(self, 'txtKeyB%d' % i).setText("FF")
        elif sender == self.btnReadBlock.objectName():
            sector = self.spnSector.value()
            block = self.spnBlock.value()
            cmd = command.read_block_cmd(sector, block)
            data = self.transmit(cmd)
            i = 0
            for val in data.split():
                if self.cbASCII.isChecked():
                    val = self.get_ascii_value(val)
                getattr(self, 'txtBlock%d' % i).setText(val)
                i += 1
        elif sender == self.btnWriteBlock.objectName():
            sector = self.spnSector.value()
            block = self.spnBlock.value()
            cmd = command.write_block_cmd(sector, block)
            for i in range(0, 16):
                attr = getattr(self, "txtBlock%d" % i)
                val = attr.text()
                if self.cbASCII.isChecked():
                    val = self.get_hexa_value(val)
                cmd += " %s" % val
            self.transmit(cmd)
        elif sender == self.cbASCII.objectName():
            # import bytes
            for i in range(0, 16):
                attr = getattr(self, 'txtBlock%d' % i)
                val = attr.text()
                if self.cbASCII.isChecked():
                    attr.setMaxLength(1)
                    attr.setText(self.get_ascii_value(val))
                else:
                    attr.setMaxLength(2)
                    attr.setText(self.get_hexa_value(val))
        elif sender == self.btnClearLog.objectName():
            self.txtAPDULog.clear()

    # -------------------------------------------------------------------------
    # ************************ Helper function is here ************************
    # -------------------------------------------------------------------------
    def connect_picc(self):
        try:
            self.current_connection.connect()
            uid = self.transmit(command.UID)
            atr = toHexString(self.current_connection.getATR())
            self.txtUID.setText(uid)
            self.txtATR.setText(atr)
            self.btnConnetPICC.setText("Disconnect")
            self.tabMain.setEnabled(True)
            self.is_picc_connect = True
            self.write_statusbar("Card connected")
        except NoCardException as e:
            self.write_statusbar(str(e), "red")
        except CardConnectionException as e:
            self.reload_readers()
            self.write_statusbar(str(e), "red")

    def disconnect_picc(self):
        try:
            self.current_connection.disconnect()
        except CardConnectionException:
            pass

        uid = ""
        atr = ""
        self.txtUID.setText(uid)
        self.txtATR.setText(atr)
        self.btnConnetPICC.setText("Connect")
        self.tabMain.setEnabled(False)
        self.is_picc_connect = False
        self.write_statusbar("Card disconnected", "blue")

    def get_ascii_value(self, hex_str):
        if not hex_str or hex_str == "00":
            return ""
        ascii = chr(int(hex_str, 16))
        return ascii

    def get_hexa_value(self, char):
        if not char:
            return "00"
        hexa = "%x" % ord(char)
        return hexa.upper()

    def reload_readers(self):
        self.cmbReader.clear()
        for reader in readers():
            reader_item = QtGui.QStandardItem(reader.name)
            reader_item.setData(reader)
            self.reader_model.appendRow(reader_item)

    def transmit(self, cmd):
        data, sw1, sw2 = self.current_connection.transmit(toBytes(cmd))
        status_code = toHexString([sw1, sw2])
        response = toHexString(data)

        # write status to apdu log
        apdu_request = ">> %s\n" % cmd
        apdu_response = "<< (%s) %s\n" % (status_code, response)
        self.txtAPDULog.insertPlainText(apdu_request)
        self.txtAPDULog.insertPlainText(apdu_response)
        self.txtAPDULog.insertPlainText("\n")

        # write status to statusbar
        status_color = "green" if status_code == '90 00' else "red"
        self.write_statusbar(status_code, status_color)

        return response

    def write_statusbar(self, message, color='green'):
        self.statusbar.setStyleSheet("color: %s;" % color)
        self.statusbar.showMessage(message)


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtWidgets.QApplication(sys.argv)

    # ui main
    window = MifareTools()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
