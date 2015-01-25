from PyQt4.uic import loadUi
from scapy.config import conf
from PyQt4.QtGui import QDialog, QTableWidgetItem
from Interface import interfaces, set_mode

__author__ = 'daniel'


class InterfaceSelectionUI(QDialog):
    def __init__(self, parent = None):
        super(InterfaceSelectionUI, self).__init__(parent)
        self.UI = loadUi('InterfaceSelectionDialog.ui', self)
        self.loadInterface()
        self.show()

    def loadInterface(self):
        intfs = interfaces()
        for index,intf in enumerate(intfs):
            self.UI.tableWidgetInterface.insertRow(index)
            self.UI.tableWidgetInterface.setItem(index, 0, QTableWidgetItem(intf))

    def getInterface(self):
        retVal = self.exec_()
        if retVal == QDialog.Rejected:
            return None
        widget = self.UI.tableWidgetInterface
        selectedItem = widget.selectedItems()
        if not selectedItem:
            return None
        iface = str(widget.selectedItems()[0].text())
        conf.iface = iface
        return iface

