# senoide

from pylab import *
import matplotlib.pyplot as plt

a = 1
f = 0.001


n = np.arange(0, a, f)
xn = np.sin(n/0.03)

plt.stem(n, xn)
plt.show()