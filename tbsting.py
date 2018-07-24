#!/bin/env python
#coding=utf8

import argparse
import sys
from tbsting.cpu.hwcpu  import hwcpu
from tbsting.cpu.syscpu import syscpu


def main():
    """
    main
    """

    parser = argparse.ArgumentParser(description="对机器进行体检的工具")
    parser.add_argument('-v', '--version', action='store_true', help='输出版本')
    parser.add_argument('-a', '--autorun', action='store_true', help='自动运行')
    parser.add_argument('-c', '--cpu', action='store_true', help='检查CPU')

    args = parser.parse_args()
    if args.version:
        print "version"
    elif args.cpu:
        cpuinfo_hwcpu = hwcpu()
        cpuinfo_hwcpu.auto()
        cpuinfo_syscpu= syscpu()
        cpuinfo_syscpu.auto()
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
