from subprocess import Popen, PIPE

__author__ = 'daniel'


def interfaces():
    return readProcFile()


def readProcFile():
    interfaces=[]
    with open('/proc/net/dev') as f:
        for line in f:
            if ':' in line:
                interfaces.append(line.split(':')[0].strip())

    return interfaces


def set_mode(interface, mode):
    if_down_command = ['ifconfig', interface, 'down']
    iw_monitor_command = ['iwconfig', interface, 'mode', mode]
    if_up_command = ['ifconfig', interface, 'up']

    process = Popen(if_down_command, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    if stderr is not "":
        raise Exception(stderr)
    process = Popen(iw_monitor_command, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    if stderr is not "":
        raise Exception(stderr)
    process = Popen(if_up_command,stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    if stderr is not "":
        raise Exception(stderr)

    intf, monitor = iwconfig()
    if not monitor:
        raise Exception("set to monitor failed")


def iwconfig():
    '''
    using subprocess.Popen to create a sub process to get the wireless interface
    '''
    process = Popen(['iwconfig'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    if stdout is "":
        raise Exception("can't find wireless card")
    else:
        wireless_interface = stdout.split(" ")[0]
        if "Mode:Monitor" in stdout:
            monitor = True
        else:
            monitor = False
        return wireless_interface, monitor
