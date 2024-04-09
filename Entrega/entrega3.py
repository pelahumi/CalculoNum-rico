import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1
c = -1
d = 0

M = 40
N = 40

h = (b-a)/N
k = (d-c)/M

w = [[0 for i in range(M + 1)] for j in range(N + 1)]

def f(i, j):
    return 0


for i in range(1, N):
    w[i][0] = (10*i*h)*(1 - i*h)
    w[i][M] = -5

for j in range(1, M):
    w[0][j] = 5*(c + j*k)
    w[N][j] = 5*np.sin(2*np.pi*(c + j*k))

for p in range(100):
    for i in range(1, N):
        for j in range(1, M):
            w[j][i] = (((k**2 * (c + j*k)) * (w[j][i+1] + w[j][i-1])) - ((i*h * h**2) * (w[j+1][i] + w[j-1][i]))) / (2*(k**2 * (c + j*k) - i*h * h**2))


x = np.linspace(a, b, M + 1)
y = np.linspace(c, d, N + 1)
x, y = np.meshgrid(y, x)
z = np.array(w)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('Y')
ax.set_ylabel('X')
ax.set_zlabel('Z')
ax.set_title('Superficie 3D')

plt.show()