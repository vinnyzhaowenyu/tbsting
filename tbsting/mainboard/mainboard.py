import subprocess
#coding:utf-8

class mainboard():
    def __init__(self):
        pass
    def auto(self):
        a = self.test()
        print a
    def test(self):
        ret = {}
        ret['test'] = "Hello mainboard"
        return ret
