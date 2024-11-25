import matplotlib.pyplot as plt 

import numpy as np

x = np.arange(-5,5, .01)
y = np.sin(2*np.pi*x)

plt.xlim(-5,5)
plt.ylim(-1.5,1.5)

plt.plot(x,y)

plt.grid()

plt.show()