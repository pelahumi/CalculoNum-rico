import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = 0
b = np.pi
c = 0
d = np.pi
N = 40
M = 40
h = (b - a) / N
k = (d - c) / M
w = [[0 for i in range(N + 1)] for j in range(M + 1)]

def f(i, j):
    return 0

for i in range(N):
    for j in range(M):
        w[i][j] = 0

# Aquí introducimos los datos de contorno
for i in range(1, N):
    w[i][0] = 0
    w[i][M] = 0

for j in range(1, M):
    w[0][j] = c + j * k
    w[N][j] = c + j * k

for p in range(100):
    for i in range(1, N):
        for j in range(1, M):
            w[i][j] = (k ** 2 * (w[i + 1][j] + w[i - 1][j]) + h ** 2 * (w[i][j + 1] + w[i][j - 1]) - (
                        h * k) ** 2 * f(i, j)) / (2 * (h ** 2 + k ** 2))

# Definir los puntos x, y, z para la superficie
x = np.linspace(a, b, M + 1)
y = np.linspace(c, d, N + 1)
x, y = np.meshgrid(x, y)
z = np.array(w)

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Trazar la superficie
ax.plot_surface(x, y, z, cmap='viridis')

# Configurar etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Superficie 3D')

# Mostrar el gráfico
plt.savefig('img/Poisson.png')
plt.show()