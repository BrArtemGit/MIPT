import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.1)
plt.plot(x, abs(x), 'r')
plt.plot(x, (4*x+5)*(x-3), 'b')
plt.show()