#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:56:56 2019

@author: Raph
"""

import serial
import time
import matplotlib.pyplot as plt
from pyfirmata import Arduino
from savitzky_golay import savitzky_golay


try :
    ser = serial.Serial('COM6',timeout=1,baudrate=115200)
except :
    print()


Nbdata=100000
cpt=0
rawdata=[]
while cpt<Nbdata :  #mettre autre condition, un compteur par exemple
    x = ser.readline()
    X=(str(x).split("\\")[0][2:])
    cpt+=1
    rawdata.append(X)


rawdata = [int(i) for i in rawdata[:]]


plt.plot(range(len(rawdata)),rawdata)
plt.show()

with open('0_outputs.txt','w') as f:
    for i in rawdata:
        f.write("%d\n" % i)
        
f.close()
    