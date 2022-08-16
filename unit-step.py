# degrau unitário

from pylab import *
import matplotlib.pyplot as plt

n = np.arange(-10, 10, 1)
step = (n >= 0) * 1

plt.stem(n, step)
plt.show()
