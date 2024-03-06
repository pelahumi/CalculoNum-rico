import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 5
c = 0
d = 10
v = 5

M = 400
N = 40
h = (b-a)/N
k = (d-c)/M

p = v*k/h

w = [[0 for i in range(N + 1)] for j in range(M + 1)]

def f(x):
    return x*(b-x)

def g(x):
    return 0

for j in range(1, M):
    w[j][0] = 0
    w[j][N] = 0 

for i in range(1, N):
    w[0][i] = f(i * h)
    w[1][i] = w[0][i] + k * g(i * h)

for j in range (1, M):
    for i in range(1,N):
        w[j+1][i] = 2*(1 - p**2)*w[j][i] + (p**2)*(w[j][i+1] + w[j][i-1]) - w[j-1][i]

x = np.linspace(a, b, N+1)
y = np.linspace(c, d, M+1)
x, y = np.meshgrid(x, y)
z = np.array(w)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Superficie 3D')

plt.savefig('img/Ondas.png')

plt.show()