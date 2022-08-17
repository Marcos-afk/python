# sinal exponencial

from pylab import *
import matplotlib.pyplot as plt


n = np.arange(-1, 1, 0.1)
a = 2
exp = np.exp(a*n)

plt.stem(n, exp)
plt.show()
