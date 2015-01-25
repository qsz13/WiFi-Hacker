import os
from PyQt4.QtGui import *
import sys
from InterfaceSelection import InterfaceSelection
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from MainWindow import MainWindow


def main():
    App = QApplication(sys.argv)
    ifaceSelection = InterfaceSelection()
    window = MainWindow(ifaceSelection.hoverThread)
    App.exec_()

if __name__ == "__main__":
    if os.geteuid() != 0:
        print "please open with sudo!"
        exit()
    main()