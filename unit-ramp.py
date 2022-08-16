# rampa unitária

from pylab import *
import matplotlib.pyplot as plt

n = np.arange(-2, 6, 1)
ramp = (n >= 0) * n

plt.stem(n, ramp)
plt.show()
