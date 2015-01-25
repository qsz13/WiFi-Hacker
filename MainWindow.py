from PyQt4.uic import loadUi
from scapy.config import conf
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QMainWindow
from HackAPUI import HackAPUI

from HackClientUI import HackClientUI
from HackAllUI import HackAllUI
from ScanUI import ScanUI


class MainWindow(QMainWindow):

    def __init__(self, hoverThread,parent = None):
        super(MainWindow, self).__init__(parent)
        self.hoverThread = hoverThread
        self.UI = loadUi('MainWindow.ui', self)
        self.scanUI = ScanUI(self)
        self.AP_List = self.scanUI.scan.AP_list
        self.clients_APs = self.scanUI.scan.clients_APs
        self.hackAllUI = HackAllUI(self)
        self.hackAPUI = HackAPUI(self)
        self.hackClientUI = HackClientUI(self)

        # self.client = ClientUI(self)
        self.is_hacking = False
        self.initUI()
        self.show()

    def initUI(self):
        self.tableWidgetAP.setColumnWidth(0, 150)
        self.tableWidgetAP.setColumnWidth(1, 400)
        self.tableWidgetAP.horizontalHeader().setStretchLastSection(True)
        # self.hackButton.clicked.connect(self.hackButtonClicked)

    # @pyqtSlot()
    # def hackButtonClicked(self):
    #     indexList = self.tableWidgetAP.selectionModel().selection().indexes()
    #     AP_index_list = []
    #     for index in indexList:
    #         if index.row() not in AP_index_list:
    #             AP_index_list.append(index.row())
    #
    #
    #     if not self.is_hacking:
    #         self.hack(AP_index_list)
    #         self.hackButton.setText("Stop!")
    #     else:
    #         self.stop_hack()
    #         self.hackButton.setText("Hack!")



    #
    # def hack(self, index_list):
    #     if not self.is_hacking:
    #        AP_list = self.scanUI.scan.AP_list
    #        self.hackThread = HackThread(index_list, AP_list)
    #        self.hackThread.start()
    #        self.is_hacking = True
    #
    # def stop_hack(self):
    #     print "STOP!!!!"
    #     self.hackThread.flag = True
    #     self.is_hacking = False