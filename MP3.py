import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0, 50, 10)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='Temps(10s)', ylabel='température (°)',
       title='Température en fonction du temps')
ax.grid()

fig.savefig("test.png")
plt.show()