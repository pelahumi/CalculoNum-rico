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

w = np.zeros((N+1, M+1))

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
            #w[j][i] = (((k**2 * (c + j*k)) * (w[j][i+1] + w[j][i-1])) - ((i*h * h**2) * (w[j+1][i] + w[j-1][i]))) / (2*(k**2 * (c + j*k) - i*h * h**2))
            w[i][j]= (i*h**3*(w[i][j+1]+w[i][j-1])-(-1+j*k)*k**2*(w[i+1][j]+w[i-1][j]))/(2*(k**2-k**3*j+h**3*i))


x = np.linspace(a, b, N+1) 
t = np.linspace(c, d, M+1) 
X, T = np.meshgrid(x, t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, T, w.T, cmap='viridis', edgecolor='none')  
ax.set_title('Superficie 3D de la Matriz w')
ax.set_xlabel('X')
ax.set_ylabel('T')
ax.set_zlabel('w')

fig.colorbar(surf)
plt.show()