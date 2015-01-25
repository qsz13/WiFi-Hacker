from PyQt4.QtCore import QObject, pyqtSlot
from HackClient import HackClient

__author__ = 'daniel'

class HackClientUI(QObject):
    def __init__(self, parent = None):
        super(HackClientUI, self).__init__(parent)
        self.parent = parent

        self.hackClientButton = self.parent.hackClientButton
        self.clientLineEdit = self.parent.clientLineEdit
        self.apLineEdit = self.parent.apLineEdit
        self.is_hacking = False
        self.initUI()
        self.scan = self.parent.scanUI.scan
        self.clientAttack = HackClient(self, self.parent.AP_List)

    def initUI(self):
        self.hackClientButton.clicked.connect(self.hackClientButtonClicked)


    @pyqtSlot()
    def hackClientButtonClicked(self):
        if not self.is_hacking:
            client_mac = str(self.clientLineEdit.text())
            ap_mac = str(self.apLineEdit.text())
            self.clientAttack.start_attack_client(ap_mac, client_mac)
            self.hackClientButton.setText("Stop!")
            self.is_hacking = True
        else:
            self.clientAttack.stop_attack_client()
            self.hackClientButton.setText("Hack!")
            self.is_hacking = False

