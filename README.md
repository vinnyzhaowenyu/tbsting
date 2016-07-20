# Tbsting (Trouble Shooting)
# 问题定位

或取系统信息并快速分析定位   

# 整体架构思路
程序采用C/S架构获取和处理数据，录入和输出由Web系统提供。

### Client
Client(客户端)负责发放到目标主机，负责采集数据和上报数据。

### Server
Server(服务端)负责收集Client上传的数据并入库，分析并定位问题。

### Web
Web(网站系统)负责接收任务和展示分析定位结果。

# 详细思路解释  

### Client
客户端负责数据的收集，主要收集的信息有：   

- CPU

- Disk

- Memory

- BIOS

- MainBoard

- Power

- NIC

- Fan

- 


