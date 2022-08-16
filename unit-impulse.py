# impulso unitário

from pylab import *
import matplotlib.pyplot as plt

n = np.arange(-10, 10, 1)
impulse = (n == 0) * 1

plt.stem(n, impulse)
plt.show()
