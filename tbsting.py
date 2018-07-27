#!/bin/env python
#coding=utf8

import argparse
import sys
from tbsting.cpu.hwcpu  import hwcpu
from tbsting.cpu.syscpu import syscpu
from tbsting.fan.hwfan  import hwfan
from tbsting.disk.battery import battery
from tbsting.memory.sysmem import sysmem
from tbsting.kernel.proc_sys import proc_sys
from tbsting.network.network import network
from tbsting.syslog.dmesg import dmesg
from tbsting.bios.bios import bios
from tbsting.power.power import power
from tbsting.mainboard.mainboard import mainboard
from tbsting.service.service import ntp
from tbsting.service.service import cron
from tbsting.service.service import ssh


def main():
    """
    main
    """

    parser = argparse.ArgumentParser(description="对机器进行体检的工具")
    parser.add_argument('-a', '--autorun', action='store_true', help='自动运行')
    parser.add_argument('-b', '--bios', action='store_true', help='检查bios')
    parser.add_argument('-c', '--cpu', action='store_true', help='检查CPU')
    parser.add_argument('-d', '--disk', action='store_true', help='检查磁盘')
    parser.add_argument('-f', '--fan', action='store_true', help='检查风扇')
    parser.add_argument('-k', '--kernel', action='store_true', help='检查Kernel')
    parser.add_argument('-m', '--memory', action='store_true', help='检查内存')
    parser.add_argument('-mb', '--mainboard', action='store_true', help='检查主板')
    parser.add_argument('-n', '--network', action='store_true', help='检查Network')
    parser.add_argument('-p', '--power', action='store_true', help='检查power')
    parser.add_argument('-s', '--syslog', action='store_true', help='检查系统日志')
    parser.add_argument('-sv', '--service', action='store_true', help='检查服务日志')
    parser.add_argument('-v', '--version', action='store_true', help='输出版本')

    args = parser.parse_args()
    if args.version:
        print "version"
    elif args.cpu:
        cpuinfo_hwcpu = hwcpu()
        cpuinfo_hwcpu.auto()
        cpuinfo_syscpu= syscpu()
        cpuinfo_syscpu.auto()
    elif args.fan:
        faninfo_hwfan = hwfan()
        faninfo_hwfan.auto()
    elif args.disk:
        diskinfo_battery = battery()
        diskinfo_battery.auto()
    elif args.memory:
        meminfo_sysmem = sysmem()
        meminfo_sysmem.auto()
    elif args.kernel:
        proc_sys().auto()
    elif args.network:
        network().auto()
    elif args.syslog:
        dmesg().auto()
    elif args.power:
        power().auto()
    elif args.bios:
        bios().auto()
    elif args.mainboard:
        mainboard().auto()
    elif args.service:
        ntp().auto()
        cron().auto()
        ssh().auto()
    elif args.autorun:
        print "auto"
    else:
        parser.print_help()

if __name__ == '__main__':
    """
    start
    """
    #print sys.path
    main()
