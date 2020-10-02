import serial
import matplotlib.pyplot as plt

ser = serial.Serial("COM7",baudrate =9600)
i = 0

while True:
    temperature = ser.readline()
    print(i, temperature)
    if i%2==0 and i > 17:
        temperature = temperature.decode("ascii").rstrip()
        print(temperature)
    i += 1
    

