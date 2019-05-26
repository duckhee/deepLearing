import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
	return 1 / (1+np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))

t = np.array([1.0, 2.0, 3.0])
tmp = 1 + t

tmp2 = 1.0 / t

x1 = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x1)
plt.plot(x1, y)
plt.ylim(-0.1, 1.1)

plt.show()
