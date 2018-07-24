#_*_ coding:utf-8 _*_
import subprocess
import re
import time
import psutil

class syscpu():
    def __init__(self):
        pass

    def auto(self):
        print self.cpu_count()
        print self.cpu_percent()
        print self.cpu_stats()
        print self.cpu_times()
        print self.cpu_times_percent()
    #    print self.cpu_freq()
        print self.loadavg()

    def cpu_count(self):
        ret = {}
        ret['physical_cpu_count'] =  psutil.cpu_count(logical=False)
        ret['logical_cpu_count'] = psutil.cpu_count() 
        return ret 
  
    def cpu_percent(self):
        ret = {}
        ret['total_cpu_percent'] = psutil.cpu_percent(percpu=False)
        ret['per_cpu_percent'] = psutil.cpu_percent(percpu=True)
        return ret

    def cpu_stats(self):
        ret = {}
        ret['cpu_ctx_switches'] = psutil.cpu_stats().ctx_switches
        ret['cpu_interrupts']  = psutil.cpu_stats().interrupts
        ret['cpu_soft_interrupts'] = psutil.cpu_stats().soft_interrupts
        ret['cpu_syscalls'] = psutil.cpu_stats().syscalls
        return ret

    def cpu_times(self):
        ret = {}
        ret['cpu_user'] = psutil.cpu_times().user
        ret['cpu_nice'] = psutil.cpu_times().nice
        ret['cpu_system'] = psutil.cpu_times().system
        ret['cpu_idle'] = psutil.cpu_times().idle
        ret['cpu_iowait'] = psutil.cpu_times().iowait
        ret['cpu_irq'] = psutil.cpu_times().irq
        ret['cpu_softirq'] = psutil.cpu_times().softirq
        ret['cpu_steal'] = psutil.cpu_times().steal
        ret['cpu_guest'] = psutil.cpu_times().guest
        ret['cpu_guest_nice'] = psutil.cpu_times().guest_nice
        return ret

    def cpu_times_percent(self):
        ret = {}
        ret['cpu_percent_user'] = psutil.cpu_times_percent().user
        ret['cpu_percent_nice'] = psutil.cpu_times_percent().nice
        ret['cpu_percent_system'] = psutil.cpu_times_percent().system
        ret['cpu_percent_idle'] = psutil.cpu_times_percent().idle
        ret['cpu_percent_iowait'] = psutil.cpu_times_percent().iowait
        ret['cpu_percent_irq'] = psutil.cpu_times_percent().irq
        ret['cpu_percent_softirq'] = psutil.cpu_times_percent().softirq
        ret['cpu_percent_steal'] = psutil.cpu_times_percent().steal
        ret['cpu_percent_guest'] = psutil.cpu_times_percent().guest
        ret['cpu_percent_guest_nice'] = psutil.cpu_times_percent().guest_nice
        return ret

    #def cpu_freq(self):
    #    return psutil.cpu_freq()

    def loadavg(self):
        try:
            f = open("/proc/loadavg", "r")
            c = f.readline().strip()
        except:
            pass
        finally:
            f.close()

        d = c.split()
        ret = {}
        ret['load1'] = d[0]
        ret['load5'] = d[1]
        ret['load15'] = d[2]
        return ret 
