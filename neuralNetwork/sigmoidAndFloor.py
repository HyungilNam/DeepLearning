print('계단 함수(점선)와 시그모이드 함수(실선)')

import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / ( 1 + np.exp(-x))

def step_function(x):
    return np.array(x>0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)

y1 = step_function(x)
y2 = sigmoid(x)

plt.plot(x, y1, linestyle ="--", label = "step_function")
plt.plot(x, y2, label = "sigmoid")

plt.ylim(-0.1, 1.1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("step_function and sigmoid")
plt.legend()
plt.show()
