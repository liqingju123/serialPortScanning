#encoding:utf-8
   
import serial  
import serial.tools.list_ports  
from time import sleep


'''
扫描可用串口号
'''   
def scanning_port():
    port_list = list(serial.tools.list_ports.comports())  
     
    print len(port_list)  
    if len(port_list) <= 0:  
        print "暂未找到开放串口"  
           
    else:  
        for one_port_list in port_list:
            port_list_0 =list(one_port_list)
            port_serial = port_list_0[0]  
            ser = serial.Serial(port_serial,9600,timeout = 1)  
            print "可用串口名称   ",ser.name 
'''
测试读取 串口数据
'''
def read_port():
    ser = serial.Serial('/dev/cu.usbserial', 19200, timeout=1)
    print '====='
    while True: 
        line = ser.readlines()
        if len(line) >0:
            print line,
        else:
            sleep(1)
    
    

