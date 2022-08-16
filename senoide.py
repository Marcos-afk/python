# senoide

from pylab import *
import matplotlib.pyplot as plt

fs = 44100
ts = 1 / fs
f0 = 440

n = np.arange(44100)
xn = np.cos(2 * np.pi * n * f0 * ts)


fig = plt.figure(figsize=(5, 5))
ax = plt.axes(projection=None)
ax.scatter(n[0:200]*ts, xn[0:200])
plt.show()
