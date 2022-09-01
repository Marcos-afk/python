import matplotlib.pyplot as plot
import numpy as np

Fs = 8000
f0 = 100
N = int(Fs/f0)

# vetor que armazenará os pontos do tempo
time = np.linspace(0, 0.02, 800)


# calculos de tempo e frequência
delta = (4.5 - (-4.5))/16
amplitude = 4.5*np.sin(2.5*np.pi*100*time)
plot.plot(time, amplitude)

# será a voltagem máxima dos pisos
v = []

for a in amplitude:
    # calculo di ínidice do código binário
    i = round((a-(-5))/delta)
    # calculo dos pisos
    v.append(-5+i*delta)


plot.step(time, v)
plot.show()