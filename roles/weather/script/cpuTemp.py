#!/usr/bin/python
# @engelrico
# read CPUtemp and push to influx

import re, commands
import requests


def check_CPU_temp():
    temp = None
    err, msg = commands.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg)   # https://stackoverflow.com/a/49563120/3904031
        try:
            temp = float(m.group())
        except:
            pass
    return temp, msg

temp, msg = check_CPU_temp()

data = 'garden_cpu_temp,host=dobby,location=roaming value=' + str(temp)
#print data
output = requests.post('http://192.168.188.29:8086/write?db=home', data=data)

#print "temperature (" + u'\xb0' + "C): ", temp
#print "full message:    ", msg
