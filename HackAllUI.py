from PyQt4.QtCore import QObject, pyqtSlot
from HackAll import HackAll

__author__ = 'daniel'


class HackAllUI(QObject):
    def __init__(self, parent = None):
        super(HackAllUI, self).__init__(parent)
        self.parent = parent
        self.oneKeyButton = self.parent.oneKeyButton
        self.hackAll = HackAll(self)
        self.is_hacking = False
        self.initUI()

    def initUI(self):
         self.oneKeyButton.clicked.connect(self.oneKeyButtonClicked)

    @pyqtSlot()
    def oneKeyButtonClicked(self):
        if not self.is_hacking:
            self.hackAll.hack_all()
            self.oneKeyButton.setText("Stop!")
            self.is_hacking = True

        else:
            self.hackAll.stop_hack_all()
            self.oneKeyButton.setText("One Key Hack!")
            self.is_hacking = False

