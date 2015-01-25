from scapy.layers.dot11 import Dot11Elt
import threading
from scapy.all import *

class ScanThread(threading.Thread):
    def __init__(self, scanObj):
        threading.Thread.__init__(self)
        self.sacnObj = scanObj
        self.flag = False
        self.daemon = True

    def run(self):
        for i in range(0,100):
            while True:
                try:
                    sniff(prn=self.recv, iface=conf.iface)
                except Exception as e:
                    print str(e)+"!@#!@#!@#!@#"
                    continue
                break






    def recv(self, packet):
        if self.flag:
            raise Exception('Stop Packet Scan')
        try:
            self.sacnObj.append_packet_list(packet)
        except Exception as e:
            print "recv: " + str(e)
        pass