# _*_ coding=utf-8 _*_
import psutil

class hwfan():
    def __init__(self):
        pass

    def auto(self):
        v = self.sensors_fans 
        print "fan info: %s" % v

    def sensors_fans(self):
        return psutil.sensors_fans()
