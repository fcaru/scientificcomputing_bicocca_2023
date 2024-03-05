import numpy as np
import matplotlib.pyplot as plt

N = 256
x = np.linspace(-2, 2, N)
y = np.linspace(-2, 2, N)

xv, yv = np.meshgrid(x, y, indexing="ij")

c = xv + 1j*y

z = np.zeros((N, N), dtype=np.complex128)
m = np.zeros((N, N))

for i in range(1,10000):
    print(f'Iteration {i}')
    z = z**2 + c
    m[np.abs(z)<=2] = i

    if np.all(m!=0):
        break

fig, ax = plt.subplots()
im = ax.imshow(m)
fig.colorbar(im)

plt.show()