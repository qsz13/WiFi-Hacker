from PyQt4.uic import loadUi
from PyQt4.QtCore import QObject, pyqtSlot
from PyQt4.QtGui import QDialog, QTableWidgetItem, QToolButton, QTextCursor
from Scan import Scan

__author__ = 'daniel'

class ScanUI(QObject):
    def __init__(self, parent = None):
        super(ScanUI, self).__init__(parent)
        self.parent = parent
        self.scan = Scan(self)


    def add_ap(self, packet):
        tableWidgetAP = self.parent.tableWidgetAP
        count = tableWidgetAP.rowCount()
        tableWidgetAP.insertRow(count)
        tableWidgetAP.setItem(count, 0, QTableWidgetItem(packet[0]))
        tableWidgetAP.setItem(count, 1, QTableWidgetItem(packet[1]))
        tableWidgetAP.setItem(count, 2, QTableWidgetItem(packet[2]))


    def getHackAPList(self):
        retVal = self.exec_()
        if retVal == QDialog.Rejected:
            return None
        widget = self.UI.tableWidgetInterface
        return str(widget.item(widget.currentRow(), 0).text())







