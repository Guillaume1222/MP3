import serial
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

class ListFile2:

    def __init__(self) -> None:
        self.lst = []

    def get_lst(self) -> list:
        self.lst

    def is_empty(self) -> None:
        return bool(self.lst)

    def ajout(self, val) -> None:
        if not self.is_empty():
            self.lst.append(val)

    def retire(self):
        return_val = None
        if not self.is_empty():
            return_val = self.lst.pop(1)
        return return_val

    def premier(self):
        return_val = None
        if not self.is_empty():
            return_val = self.lst[0]
        return return_val

    def taille(self):
        return len(self.lst)


#Pyserial
ser = serial.Serial("COM7",baudrate =9600)

#Courbe
fig, ax = plt.subplots()

y = temperature
x = (0, 50, 10)
line, = ax.plot(x, y)


def animate(i):
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
    return line


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

F=ListFile2()
F.taille(10)
F.ajout(y)
F.retire(x)

