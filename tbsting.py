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


def main():
    """
    main
    """

    parser = argparse.ArgumentParser(description="对机器进行体检的工具")
    parser.add_argument('-v', '--version', action='store_true', help='输出版本')
    parser.add_argument('-a', '--autorun', action='store_true', help='自动运行')
    parser.add_argument('-c', '--cpu', action='store_true', help='检查CPU')
    parser.add_argument('-f', '--fan', action='store_true', help='检查风扇')
    parser.add_argument('-d', '--disk', action='store_true', help='检查磁盘')
    parser.add_argument('-m', '--memory', action='store_true', help='检查内存')
    parser.add_argument('-k', '--kernel', action='store_true', help='检查Kernel')
    parser.add_argument('-n', '--network', action='store_true', help='检查Network')

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
