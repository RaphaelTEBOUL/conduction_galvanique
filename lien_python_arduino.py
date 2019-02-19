#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:56:56 2019

@author: Raph
"""

import serial
ser = serial.Serial('/dev/ttyACM0',9600)
# cette info est donnee par l'interface java arduino
print(ser)

while True:  #mettre autre condition, un compteur par exemple
    x = ser.readline()          # read one byte
    print("data", x)
    with open("output.txt", "a") as fichier:
        ser.readline()          # read one byte
        mycollapsedstring = ' '.join(x.split())
        #print mycollapsedstring.split(':')
        fichier.write(mycollapsedstring)
        print("ecriture ok")
fichier.close()
ser.close()
