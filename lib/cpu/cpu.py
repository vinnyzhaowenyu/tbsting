#conding=utf8

import subprocess

class cpu():
    def __init__(self):
        pass
    def get_vendor(self):
        comm="cat /proc/cpuinfo |grep vendor_id"
        subprocess.check_output(comm, shell=True)
