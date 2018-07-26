import subprocess

#coding:utf-8
class network():
    def __init__(self):
        pass
    def auto(self):
        a = self.route_table()
        print a 
    def route_table(self):
        com = "ip route show"
        try:
            out = subprocess.check_output(com, shell=True).strip()
        except:
            pass

        ret = {}
        ret['route_table'] = out
        return ret
