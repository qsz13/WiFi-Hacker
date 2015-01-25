from PyQt4.QtGui import QMessageBox
from subprocess import Popen, PIPE
from HoverThread import HoverThread
from Interface import set_mode
from InterfaceSelectionUI import InterfaceSelectionUI

__author__ = 'daniel'

class InterfaceSelection():
    def __init__(self):
        self.selecting = True
        while self.selecting:
            ifaceDiag = InterfaceSelectionUI()
            interface = ifaceDiag.getInterface()
            if interface is None:
                exit()
            if self.check_is_wireless(interface):
                self.config_inface(interface)
                self.selecting = False
            else:
                QMessageBox.about(ifaceDiag, 'Attention',
            "This interface is not for wireless")
                continue


    def config_inface(self, iface):
        try:
            set_mode(iface, "monitor")
            self.hoverThread = HoverThread()
            self.hoverThread.start()
        except:
            print "config interface failed"
            raise


    def check_is_wireless(self, iface):
        if_command = ['iwconfig', iface]

        process = Popen(if_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        if stderr is not "":
            return False
        else:
            return True