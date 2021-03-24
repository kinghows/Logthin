# Logthin

Log slimming tool

Python 3.6+

###Windows

1、筛选出UDSAgent.log包含Job_0044497的行

.\Logthin.exe -l UDSAgent.log -k Job_0044497

2、筛选出udppm.log包含Job_0045069,而且包含fingerprint或Closing vdisk 的行 

.\Logthin.exe -l udppm.log -k Job_0045069  -i fingerprint,Closing vdisk

3、筛选出udppm.log包含Job_0045069,而且包含fingerprint 但不包含Periodic 的行

.\Logthin.exe -l udppm.log -k Job_0045069  -i fingerprint -e Periodic

4、筛选出udppm.log 包含fingerprint的行 

.\Logthin.exe -l udppm.log -i fingerprint

注意：

-i -e 参数可以写入执行文件同目录Logthin.ini，格式如下

[set]

including =  ORA-,RMAN-

#excluding = 

#including =  ORA-

-i -e 参数可以多个，用逗号分隔



###Linux：

 python3 Logthin.py -l UDSAgent.log -k Job_0491768




## 好用的DBA系列，喜欢的请打颗星：

- [MySQL_Watcher：数据库性能指标的HTML监控报告](https://github.com/kinghows/MySQL_Watcher)

- [SQL_Report：自定义SQL生成HTML报告](https://github.com/kinghows/SQL_Report)

- [SQL_Chart：自定义SQL生成HTML图表](https://github.com/kinghows/SQL_Chart)

- [Logthin：日志精简工具](https://github.com/kinghows/Logthin)
