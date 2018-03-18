#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 00:39:52 2018

@author: rudegentleman
"""
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
while True:
    try:
        value = ser.readline()
        print (value)
    except KeyboardInterrupt:
        break
ser.close()    
