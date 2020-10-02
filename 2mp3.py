# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:57:32 2020

@author: Elève
"""

import serial
import matplotlib.pyplot as plt


ser = serial.Serial("COM7",baudrate =9600)
i = 0

while True:
    temperature = ser.readline()
    print(i, temperature)
    if i > 17:
        if i%2==0:
            temperature = float(
                    temperature.decode("UTF-8").rstrip().split(": ")[1][0: -2]
                    )
            print(temperature)
        elif i%2==1:
            temperature = float(
                    temperature.decode("UTF-8").rstrip().split(": ")[1][0: -1]
                    )
            print(temperature)
    i += 1


