# Tbsting (Trouble Shooting)

## Linux系统问题定位工具(系统体检)

或取系统信息并快速分析定位出异常情况，通过和配置标准进行对比，判断系统运行健康状况。

分析后生产报表，输出为EXCEL/HTML等格式。

## 安装 

### 依赖
- Python2.6+
- Psutil
https://github.com/giampaolo/psutil.git

# 思路解释  

在物理层获取CPU/Disk/Memory/BIOS/MainBoard/Power/NIC/Fan的信息

在系统层获取内核、系统参数、系统日志信息

在应用层获取NTP、SSH、Crontab的服务信息

# 使用
```
[root@izj6cdhdoq5a5zsf7bf7a3z tbsting]# ./tbsting.py
usage: tbsting.py [-h] [-a] [-b] [-c] [-d] [-f] [-k] [-m] [-mb] [-n] [-p] [-s]
                  [-sv] [-v]

对机器进行体检的工具

optional arguments:
  -h, --help        show this help message and exit
  -a, --autorun     自动运行
  -b, --bios        检查bios
  -c, --cpu         检查CPU
  -d, --disk        检查磁盘
  -f, --fan         检查风扇
  -k, --kernel      检查Kernel
  -m, --memory      检查内存
  -mb, --mainboard  检查主板
  -n, --network     检查Network
  -p, --power       检查power
  -s, --syslog      检查系统日志
  -sv, --service    检查服务日志
  -v, --version     输出版本
```
