#_*_ coding:utf-8 _*_
import subprocess
import re
import time
import psutil

class syscpu():
    def __init__(self):
        pass

    def auto(self):
        count = self.cpu_count()
        percent = self.cpu_percent()
        stats = self.cpu_stats()
        times = self.cpu_times()
        times_percent = self.cpu_times_percent()
    #    print self.cpu_freq()
        loadavg = self.loadavg()
        print "物理CPU核数: %s " % count['physical_cpu_count']
        print "逻辑CPU核数: %s " % count['logical_cpu_count']
        print "CPU整体使用率: %s " % percent['total_cpu_percent']
        print "每个CPU使用率: %s " % percent['per_cpu_percent']
        print "cpu_ctx_switches: %s " % stats['cpu_ctx_switches']
        print "cpu_interrupts: %s " % stats['cpu_interrupts']
        print "cpu_soft_interrupts: %s " % stats['cpu_soft_interrupts']
        print "cpu_syscalls: %s " % stats['cpu_syscalls']
        print "cpu_user: %s " % times['cpu_user']
        print "cpu_nice: %s " % times['cpu_nice']
        print "cpu_system: %s " % times['cpu_system']
        print "cpu_idle: %s " % times['cpu_idle']
        print "cpu_iowait: %s" % times['cpu_iowait']
        print "cpu_irq: %s" % times['cpu_irq']
        print "cpu_softirq: %s" % times['cpu_softirq']
        print "cpu_steal: %s" % times['cpu_steal']
        print "cpu_guest: %s" % times['cpu_guest']
        print "cpu_guest_nice: %s" % times['cpu_guest_nice']
        print "cpu_percent_user: %s" % times_percent['cpu_percent_user']
        print "cpu_percent_nice: %s" % times_percent['cpu_percent_nice']
        print "cpu_percent_system: %s" % times_percent['cpu_percent_system']
        print "cpu_percent_idle: %s" % times_percent['cpu_percent_idle']
        print "cpu_percent_iowait: %s" % times_percent['cpu_percent_iowait']
        print "cpu_percent_irq: %s" % times_percent['cpu_percent_irq']
        print "cpu_percent_softirq: %s" % times_percent['cpu_percent_softirq']
        print "cpu_percent_steal: %s" % times_percent['cpu_percent_steal']
        print "cpu_percent_guest: %s" % times_percent['cpu_percent_guest']
        print "cpu_percent_guest_nice: %s" % times_percent['cpu_percent_guest_nice']
        print "1分钟负载: %s" % loadavg['load1']
        print "5分钟负载: %s" % loadavg['load5']
        print "15分钟负载: %s" % loadavg['load15']

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
