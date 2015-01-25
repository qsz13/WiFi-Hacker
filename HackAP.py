from HackThread import HackAPThread

__author__ = 'daniel'

class HackAP:
    def __init__(self, ui_obj):
        self.ui_obj = ui_obj
        self.is_hacking = False
        self.thread = self.ui_obj.parent.hoverThread

    def hack_AP(self, index_list):
        all_AP_list = self.ui_obj.parent.AP_List
        clients_APs = self.ui_obj.parent.clients_APs
        AP_list = []
        print all_AP_list
        print index_list
        for i in index_list:
            AP_list.append(all_AP_list[i])

        # self.hackAPThread = HackAPThread(AP_list , clients_APs)
        # self.hackAPThread.start()
        self.is_hacking = True

        self.thread.is_hacking = True
        self.thread.mode = "AP"
        self.thread.ap_list = AP_list
        self.is_hacking = True

    def stop_hack_AP(self):
        # self.hackAPThread.flag = True
        self.is_hacking = False
        self.thread.is_hacking = False
