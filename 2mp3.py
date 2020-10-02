import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class ListFile2:

    def __init__(self, lengh_max: int = None) -> None:
        self.lst = []
        self.max_lengh = lengh_max

    def get_lst(self) -> list:
        return self.lst

    def get_max_lengh(self):
        return self.max_lengh

    def is_empty(self) -> None:
        return not bool(self.lst)

    def add(self, val) -> None:
        self.lst.append(val)
        if self.get_max_lengh() is not None and \
                self.lengh() > self.get_max_lengh():
            self.remove()

    def remove(self):
        return_val = None
        if not self.is_empty():
            return_val = self.lst.pop(0)
        return return_val

    def first(self):
        return_val = None
        if not self.is_empty():
            return_val = self.lst[0]
        return return_val

    def lengh(self):
        return len(self.lst)


#Pyserial
ser = serial.Serial("COM7",baudrate =9600)

#Courbe
fig, ax = plt.subplots()

x = ListFile2(10)
y = ListFile2(10)
y2 = ListFile2(10)
line, = ax.plot(x.get_lst(), y.get_lst())
line2, = ax.plot(x.get_lst(), y2.get_lst())


def animate(i):
    temperature = ser.readline()
    if i > 17 and i % 2 == 0:
        x.add(- x.get_max_lengh() + (i-1))
        temperature = float(
                temperature.decode("UTF-8").rstrip().split(": ")[1][0: -2]
                )
        y.add(temperature)
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

F=ListFile2()