from HackThread import HackAllThread

__author__ = 'daniel'

class HackAll:
    def __init__(self, ui_obj):
        self.ui_obj = ui_obj
        self.is_hacking = False
        self.thread = self.ui_obj.parent.hoverThread

    def hack_all(self):
        if not self.is_hacking:
            AP_list = self.ui_obj.parent.AP_List
            #print AP_list
            # self.hackAllThread = HackAllThread(AP_list)
            # self.hackAllThread.start()
            self.thread.is_hacking = True
            self.thread.mode = "ALL"
            self.thread.ap_list = AP_list
            self.is_hacking = True

    def stop_hack_all(self):
        # self.hackAllThread.flag = True
        self.is_hacking = False
        self.thread.is_hacking = False

