#conding=utf8

import subprocess

class hwcpu():
    def __init__(self):
        pass

    def auto(self):
        v=self.vendor()
        m=self.model_name()
        s=self.siblings()
        print v
        print m
        print s

    def vendor(self):
        com="grep vendor_id /proc/cpuinfo|sort|uniq"
        out = subprocess.check_output(com, shell=True).strip()
        ret = out.split()
        del ret[1]
        return ret 

    def model_name(self):
        com = "grep 'model name' /proc/cpuinfo|sort|uniq"
        out = subprocess.check_output(com, shell=True).strip()
        out2 = out.split(':')
        out2[1].lstrip()
        ret = []
        ret.append("model_name")
        ret.append(out2[1])
        return ret

    def siblings(self):
        com = "grep 'siblings' /proc/cpuinfo|sort|uniq"
        out = subprocess.check_output(com, shell=True).strip()
        ret = out.split()
        del ret[1]
        return ret
