# encoding:utf-8

'''
Created on 2018年3月27日

@author: imac
'''
import serial

ser = serial.Serial('/dev/ttyUSB0', 250000, timeout=1)



print ser.isOpen()
words="gggggggggggggggg"