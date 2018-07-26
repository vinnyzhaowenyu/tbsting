#coding:utf-8

class proc_sys():
    def __init__(self):
        pass
    def auto(self):
        a = self.proc_sys_net()
        print a
    def proc_sys_net(self):
        try:
            f = open("/proc/sys/net/ipv4/ip_forward", "r")
            c = f.readline().strip()
        except:
            pass
        finally:
            f.close() 
        return c
