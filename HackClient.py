from HackThread import HackClientThread

__author__ = 'daniel'

class HackClient():
    def __init__(self, ui_obj, AP_List):
        self.ui_obj = ui_obj
        self.AP_List = AP_List
        self.thread = self.ui_obj.parent.hoverThread

    def start_attack_client(self, ap ,client):
        # self.hackClientThread = HackClientThread()
        # self.hackClientThread.set_client(client)
        # self.hackClientThread.set_AP_list(self.AP_List)
        # self.hackClientThread.start()
        channel = 1
        for a in self.AP_List:
            if a[0] == ap:
                channel = int(a[1])


        self.thread.is_hacking = True
        self.thread.mode = "CLIENT"
        # self.thread.ap_list = self.AP_List
        self.thread.client = client
        self.thread.ap = [ap,channel]
        self.is_hacking = True




    def stop_attack_client(self):
        # self.hackClientThread.flag = True
        self.thread.is_hacking = False
