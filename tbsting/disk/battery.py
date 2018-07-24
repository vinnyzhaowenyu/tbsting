#_*_ coding:utf-8 _*_
import psutil

class battery():
    def __init__(self):
        pass
    def auto(self):
        a = self.sensors_battery()
        print "sensors_battery: %s "  % a

    def sensors_battery(self):
        return psutil.sensors_battery()
