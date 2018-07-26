import subprocess
#coding:utf-8

class dmesg():
    def __init__(self):
        pass

    def auto(self):
        a = self.dmesg()
        print a

    def dmesg(self):
        com = "dmesg"
        try:
            out = subprocess.check_output(com, shell=True).strip()
        except:
            pass

        ret = {}
        ret['dmesg'] = out
        return ret
