#conding=utf8

import subprocess

class hwcpu():
    def __init__(self):
        pass

    def auto(self):
        v=self.vendor()
        m=self.model_name()
        s=self.siblings()
        aa=self.vm_support()
        print aa
        print v
        print m
        print s

    def vendor(self):
        com="grep vendor_id /proc/cpuinfo|sort|uniq"
        try:
            out = subprocess.check_output(com, shell=True).strip()
        except:
            pass
        ret = {}
        ret['vendor_id'] = out.split()[2]
        return ret 

    def model_name(self):
        com = "grep 'model name' /proc/cpuinfo|sort|uniq"
        try:
            out = subprocess.check_output(com, shell=True).strip()
        except:
            pass

        out2 = out.split(':')
        out2[1].lstrip()

        ret = {}
        ret['model_name'] = out2[1]
        return ret

    def siblings(self):
        com = "grep 'siblings' /proc/cpuinfo|sort|uniq"
        try:
            out = subprocess.check_output(com, shell=True).strip()
        except:
            pass

        ret = {}
        ret['siblings'] = out.split()[2]
        return ret

    def vm_support(self):
        com = "grep -iE 'vmx|smx' /proc/cpuinfo"
        ret = {}
        ret['vm_support'] = True
        try:
            out = subprocess.check_output(com, shell=True).strip()
        except:
            ret['vm_support'] = False
        return ret
