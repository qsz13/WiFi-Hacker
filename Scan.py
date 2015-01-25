from scapy.layers.dot11 import Dot11, Dot11Elt, Dot11Beacon, Dot11ProbeResp
from threading import Lock
import Channel
from Interface import set_mode
from ScanThread import ScanThread

__author__ = 'daniel'


class Scan:
    def __init__(self, ui_obj):
        # self.packet_list = []
        self.APs = []
        self.AP_list = self.APs
        self.clients_APs = []
        self.lock = Lock()
        self.scanThread = ScanThread(self)

        self.ui_obj = ui_obj
        self.start_scan()

    def start_scan(self):
        self.scanThread.start()

    def stop_scan(self):
        self.scanThread.flag = True




    # def append_packet_list(self, pkt):
    #     print self.client_list
    #     with self.lock:
    #         self.packet_list.append(pkt)
    #     if pkt.haslayer(Dot11) and pkt.haslayer(Dot11Elt): #if the packet has 802.11 layer
    #         if pkt.addr1 and pkt.addr2:
    #             if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
    #                 self.APs_add(pkt)
    #             if pkt.type in [1, 2]:
    #                 self.clients_APs_add(pkt)
    #
    # def APs_add(self, pkt):
    #     ssid  = pkt[Dot11Elt].info
    #     bssid = pkt[Dot11].addr3
    #     try:
    #         # Thanks to airoscapy for below
    #         ap_channel = str(ord(pkt[Dot11Elt:3].info))
    #         # Prevent 5GHz APs from being thrown into the mix
    #         if int(ap_channel) > 11:
    #             return
    #
    #     except Exception as e:
    #         print e
    #         return
    #
    #
    #     if [bssid, ap_channel, ssid] in self.AP_list:
    #         return
    #     with self.lock:
    #         self.AP_list.append([bssid, ap_channel, ssid])
    #         self.ui_obj.add_ap([bssid, ssid,  ap_channel])
    #     print [bssid, ap_channel, ssid]
    #
    #
    #
    # def clients_APs_add(self,pkt):
    #     addr1 = pkt.addr1
    #     addr2 = pkt.addr2
    #     ap_channel = Channel.channel
    #
    #     # print ap_channel
    #     if len(self.client_list) == 0:
    #         if len(self.AP_list) == 0:
    #             with self.lock:
    #                 print [addr1, addr2, ap_channel]
    #                 return self.client_list.append([addr1, addr2, ap_channel])
    #         else:
    #             self.AP_check(addr1, addr2)
    #
    #     # Append new clients/APs if they're not in the list
    #     else:
    #         for ca in self.client_list:
    #             if addr1 in ca and addr2 in ca:
    #                 return
    #
    #         if len(self.AP_list) > 0:
    #             return self.AP_check(addr1, addr2)
    #         else:
    #             with self.lock:
    #                 print [addr1, addr2, ap_channel]
    #                 return self.client_list.append([addr1, addr2, ap_channel])
    #
    #
    # def AP_check(self, addr1, addr2):
    #     print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11"
    #     for ap in self.AP_list:
    #         if ap[0].lower() in addr1.lower() or ap[0].lower() in addr2.lower():
    #             with self.lock:
    #                 print [addr1, addr2, ap[1], ap[2]]
    #                 return self.client_list.append([addr1, addr2, ap[1], ap[2]])


    def append_packet_list(self, pkt):
        '''
        Look for dot11 packets that aren't to or from broadcast address,
        are type 1 or 2 (control, data), and append the addr1 and addr2
        to the list of deauth targets.
        '''

        # print self.clients_APs


        # We're adding the AP and channel to the deauth list at time of creation rather
        # than updating on the fly in order to avoid costly for loops that require a lock
        if pkt.haslayer(Dot11):
            if pkt.addr1 and pkt.addr2:

                # Check if it's added to our AP list
                if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
                    self.APs_add(self.clients_APs, self.APs, pkt)

                # Management = 1, data = 2
                if pkt.type in [1, 2]:

                    self.clients_APs_add(self.clients_APs, pkt.addr1, pkt.addr2)

    def APs_add(self, clients_APs, APs, pkt):
        ssid       = pkt[Dot11Elt].info
        bssid      = pkt[Dot11].addr3
        try:
            # Thanks to airoscapy for below
            ap_channel = str(ord(pkt[Dot11Elt:3].info))
            # Prevent 5GHz APs from being thrown into the mix
            chans = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
            if ap_channel not in chans:
                return

        except Exception as e:
            return

        if len(APs) == 0:
            self.ui_obj.add_ap([bssid, ssid,  ap_channel])
            with self.lock:
                return APs.append([bssid, ap_channel, ssid])

        else:
            for b in APs:
                if bssid in b[0]:
                    return
            self.ui_obj.add_ap([bssid, ssid,  ap_channel])
            with self.lock:
                return APs.append([bssid, ap_channel, ssid])

    def clients_APs_add(self, clients_APs, addr1, addr2):
        if len(clients_APs) == 0:
            if len(self.APs) == 0:
                with self.lock:
                    return clients_APs.append([addr1, addr2])
            else:
                self.AP_check(addr1, addr2)

        # Append new clients/APs if they're not in the list
        else:
            for ca in clients_APs:
                if addr1 in ca and addr2 in ca:
                    return

            if len(self.APs) > 0:
                return self.AP_check(addr1, addr2)
            else:
                with self.lock:
                    return clients_APs.append([addr1, addr2])

    def AP_check(self,addr1, addr2):
        for ap in self.APs:
            if ap[0].lower() in addr1.lower() or ap[0].lower() in addr2.lower():
                with self.lock:
                    return self.clients_APs.append([addr1, addr2, ap[1], ap[2]])
