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


try :
    ser = serial.Serial('COM6',timeout=1)
except :
    print('blablabla')


Nbdata=100;
cpt=0
rawdata=[]
while cpt<Nbdata :  #mettre autre condition, un compteur par exemple
    x = ser.readline()
    X=x.strip()
    cpt+=1
    rawdata.append(int(X))
    #time.sleep(.001)

ser.close()

print(rawdata)

plt.plot(range(len(rawdata)),rawdata)
plt.show()
