import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1
c = 0
d = 1
N = 10
M = 10
h = (b-a)/N
k = (d-c)/M
w = [[0 for i in range(N+1)] for j in range(M+1)]

def f(i, j):
    return 0

for i in range(N):
    for j in range(M):
        w[i][j] = 0

#Aquí introducimos los datos de contorno
for i in range(1, N):
    w[i][0] = 0
    w[i][M] = 0

for j in range(1, M):
    w[0][j] = 0
    w[N][j] = 1

for k in range(100):
    for i in range(1, N):
        for j in range(1, M):
            w[i][j] = (k**2*(w[i+1][j] + w[i-1][j]) + h**2*(w[i][j+1] + w[i][j-1]) - (h*k)**2*f(i, j))/(2*(h**2 + k**2))


x = np.linspace(a, b, M-1)
y = np.linspace(c, d, N-1)
x, y = np.meshgrid(x, y)
z = np.array(w)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z)

plt.show()