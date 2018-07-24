# _*_ coding=utf-8 _*_

import subprocess

class hwcpu():
    def __init__(self):
        pass

    def auto(self):
        v = self.vendor()
        s = self.siblings()
        vm = self.vm_support()
        m = self.model_name()

        print "CPU 厂商: %s" % v['vendor_id']
        print "CPU 型号: %s" % m['model_name']
        print "CPU 超线程: %s" % s['siblings']
        print "CPU 虚拟化支持: %s" % vm['vm_support']

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
