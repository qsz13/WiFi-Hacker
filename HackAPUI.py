from HackAP import HackAP

__author__ = 'daniel'
from PyQt4.QtCore import QObject, pyqtSlot
from HackAll import HackAll



class HackAPUI(QObject):
    def __init__(self, parent = None):
        super(HackAPUI, self).__init__(parent)
        self.parent = parent
        self.hackAPButton = self.parent.hackAPButton
        self.hackAP = HackAP(self)
        self.is_hacking = False
        self.initUI()

    def initUI(self):
         self.hackAPButton.clicked.connect(self.hackAPButtonClicked)

    @pyqtSlot()
    def hackAPButtonClicked(self):

        if not self.is_hacking:

            indexList = self.parent.tableWidgetAP.selectionModel().selection().indexes()
            AP_index_list = []
            for index in indexList:
                if index.row() not in AP_index_list:
                    AP_index_list.append(index.row())



            self.hackAP.hack_AP(AP_index_list)
            self.hackAPButton.setText("Stop!")
            self.is_hacking = True

        else:
            self.hackAP.stop_hack_AP()
            self.hackAPButton.setText("Hack!")
            self.is_hacking = False

