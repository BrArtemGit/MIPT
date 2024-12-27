import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(-5.0, 5.0, 0.1)
# s = np.sin(2 * np.pi * t)
s = t**5 + t**4 + t**3 + t**2 + t + 1
fig, ax = plt.subplots()
ax.plot(t, s)

ax.grid()

plt.show()