# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from scapy.all import *
# from scapy.layers.dot11 import *
#
# from PyQt4 import QtCore, QtGui, uic
# from PyQt4.QtGui import QMessageBox, QInputDialog, QLineEdit
# from subprocess import Popen, PIPE
# import fcntl, socket, struct
# import os
# import time
#
#
# config.verb = 0
# ap_list = []
# selected_interface = ""
# password = ""
# is_su = False
#
# def hover(interface):
#     try:
#
#         for i in range(1, 12):
#             time.sleep(1)
#             switch_channel(interface, i)
#     except KeyboardInterrupt:
#         print "quit"
#
#
# def switch_channel(interface, channel):
#     os.system("iw dev "+interface+" set channel "+str(channel))
#
#
#
#
# def uploadPacket(pkt):
#     global ap_list, MainWindow
#     if pkt.haslayer(Dot11): #if the packet has 802.11 layer
#         if pkt.type == 0 and pkt.subtype == 8:
#             ap_channel = str(ord(pkt[Dot11Elt:3].info))
#             if pkt.addr2 not in ap_list:
#                 ap_list.append(pkt.addr2)
#                 print "AP MAC: %s with SSID: %s " %(pkt.addr2, pkt.info)
#
# def check_sudo():
#     if os.getuid() != 0:
#         return False
#     else:
#         return True
#
#
# class MainWindow(QtGui.QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         uic.loadUi('MainWindow.ui', self)
#         # self.get_password()
#         self.show()
#         # hover_thread = threading.Thread(target=hover, args=[get_interface().interface])
#         # hover_thread.daemon = True
#         # hover_thread.start()
#         # sniff(iface="wlan0", prn = uploadPacket)
#         # self.update_ap_list()
#     def get_password(self):
#         global password, is_su
#         is_su = check_sudo()
#         if not is_su:
#             password, ok = QtGui.QInputDialog.getText(self , 'Permission',
#             'please input your password:', mode=QLineEdit.Password)
#             password = str(password)+'\n'
#             if not ok:
#                 exit()
#
#     def update_ap_list(self):
#         print "!"
#
#
#
#
#
#
#
#
# class WirelessInterface:
#
#     def __init__(self, interface, monitor):
#         self.monitor_mode = monitor
#         self.interface = interface
#         if not self.monitor_mode:
#             try:
#                 self.set_mode(self.interface, 'monitor')
#             except Exception as e:
#                 print e
#         self.mac_address = self.getHwAddr(interface)
#         print self.mac_address
#
#     def set_mode(self, interface, mode):
#         global password
#
#         if_down_command = ['ifconfig', interface, 'down']
#         iw_monitor_command = ['iwconfig', interface, 'mode', mode]
#         if_up_command = ['ifconfig', interface, 'up']
#         process = Popen(if_down_command, stdout=PIPE, stderr=PIPE)
#         stdout, stderr = process.communicate(password)
#         if stderr is not "":
#             raise Exception(stderr)
#         process = Popen(iw_monitor_command, stdout=PIPE, stderr=PIPE)
#         stdout, stderr = process.communicate(password)
#         print stdout
#         if stderr is not "":
#             raise Exception(stderr)
#         process = Popen(if_up_command,stdout=PIPE, stderr=PIPE)
#         stdout, stderr = process.communicate(password)
#         if stderr is not "":
#             raise Exception(stderr)
#
#         intf, monitor = iwconfig()
#         if monitor:
#             self.monitor_mode = True
#         else:
#             self.monitor_mode = False
#             raise Exception("set to monitor failed")
#
#
#
#     def getHwAddr(self,ifname):
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
#         return ':'.join(['%02x' % ord(char) for char in info[18:24]])
#
#
# def get_interface():
#     try:
#         interface, monitor = iwconfig()
#         wireless_interface = WirelessInterface(interface, monitor)
#
#         return wireless_interface
#     except Exception as e:
#         print e
#
#
# def iwconfig():
#     '''
#     using subprocess.Popen to create a sub process to get the wireless interface
#     '''
#     process = Popen(['iwconfig'], stdout=PIPE, stderr=PIPE)
#     stdout, stderr = process.communicate()
#     print stdout
#     if stdout is "":
#         raise Exception("can't find wireless card")
#     else:
#         wireless_interface = stdout.split(" ")[0]
#
#         if "Mode:Monitor" in stdout:
#             monitor = True
#         else:
#             monitor = False
#         return wireless_interface, monitor
#
#
# if __name__ == "__main__":
#     if os.geteuid() != 0:
#         print "please open with sudo!"
#         exit()
#     app = QtGui.QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sniff(iface="wlan0", prn = uploadPacket)
#     sys.exit(app.exec_())
#
