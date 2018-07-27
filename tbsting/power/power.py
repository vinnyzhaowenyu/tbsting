import subprocess
#coding:utf-8

class power():
    def __init__(self):
        pass
    def auto(self):
        a = self.test()
        print a
    def test(self):
        ret = {}
        ret['test'] = "Hello power"
        return ret
