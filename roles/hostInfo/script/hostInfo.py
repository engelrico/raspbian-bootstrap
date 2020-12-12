#!/usr/bin/python3
# @engelrico
# read CPUtemp and push to influx

#import re, commands
import requests
import socket
import os
import psutil

cmd_shell  = 'vcgencmd measure_temp'
host       = socket.gethostname()
influx_url = 'http://192.168.188.29:8086'
influx_db  = 'home'


def getCPUtemperature():
    res = os.popen(cmd_shell).readline()
    return(res.replace("temp=","").replace("'C\n",""))
#  tt = psutil.cpu_temperature()[0]
#  return str(tt)

# Return % of CPU used by user as a character string                                
def getCPUuse():
    cpuUsage = psutil.cpu_percent(interval=0.1, percpu=False)
    return(str(cpuUsage))

# log to influxdb
def logData(key,value):
  data = key+',host='+str(host)+',location=roaming value=' + value
  print(data)
  output = requests.post(influx_url+'/write?db='+influx_db, data=data)
  print(output)

  
temp  = getCPUtemperature()
logData(str(host)+'_cpu_temp',temp)

cpu  = getCPUuse()
logData(str(host)+'_cpu_use',cpu)