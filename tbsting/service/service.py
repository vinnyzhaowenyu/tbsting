import subprocess

#coding:utf-8
class ntp():
    def __init__(self):
        pass

    def auto(self):
        a = self.test()
        print a 

    def test(self):
        com = "ntpq -np 127.0.0.1"
        try:
            out = subprocess.check_output(com, shell=True).strip()
        except:
            pass

        ret = {}
        ret['test'] = out
        return ret

    def check_ntp_offset(self):
        com = "ntpdate -q 223.5.5.5"
        try:
            out = subprocess.check_output(com, shell=True).strip()
        except:
            pass

        ret = {}
        ret['test'] = out
        return ret
        

class ssh():
    def __init__(self):
        pass
    def auto(self):
        a = self.test()
        print a
    def test(self):
        com = "ps auxf |grep ssh"
        try:
            out = subprocess.check_output(com, shell=True).strip()
        except:
            pass

        ret = {}
        ret['test'] = out
        return ret

class cron():
    def __init__(self):
        pass
    def auto(self):
        a = self.test()
        print a
    def test(self):
        com = "crontab -l"
        try:
            out = subprocess.check_output(com, shell=True).strip()
        except:
            pass

        ret = {}
        ret['test'] = out
        return ret
