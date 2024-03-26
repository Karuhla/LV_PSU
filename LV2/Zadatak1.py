import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 3, num = 2)
y = np.linspace(1, 1, num = 2)
a = np.linspace(1, 2, num = 2)
b = np.linspace(1, 2, num = 2)
c = np.linspace(2, 3, num = 2)
d = np.linspace(2, 2, num = 2)
e = np.linspace(3, 3, num = 2)
f = np.linspace(1, 2, num = 2)

plt.plot(x, y, 'b', linewidth=2, marker=".", markersize=8)
plt.plot(a, b, 'b', linewidth=2, marker=".", markersize=8)
plt.plot(c, d, 'b', linewidth=2, marker=".", markersize=8)
plt.plot(e, f, 'b', linewidth=2, marker=".", markersize=8)
plt.axis([0,4,0,4])
plt.xlabel('x os')
plt.ylabel('y os')
plt.title('Primjer')
plt.show()
