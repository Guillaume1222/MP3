# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:57:32 2020

@author: Elève
"""

import serial
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

#Pyserial
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


#Courbe
fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
