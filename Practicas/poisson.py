import numpy as np
import matplotlib.pyplot as plt

#x = a + i*h
#y = c + j*k

a = 0
b = 1
c = 0
d = 1

M = 40
N = 40

h = (b - a) / N
k = (d - c) / M

w = np.zeros((M+1, N+1))

def f(i, j):
    return 0

def g(i, j):
    return 0

# Aquí introducimos los datos de contorno u(x, j)
for i in range(1, N):
    w[0][i] = 0
    w[M][i] = 0

# Aquí introducimos los datos de contorno u(i, y)
for j in range(1, M):
    w[j][0] = 0
    w[j][N] = 1


# Método de diferencias finitas
for p in range(100):
    for j in range(1, M):
        for i in range(1, N):
            w[j][i] = (k**2 * (w[j][i+1] + w[j][i-1]) + h**2 * (w[j+1][i] + w[j-1][i]) - (
                        h * k) ** 2 * f(i, j))/(2*k**2 + 2*h**2 - 2)

# Definir los puntos x, y, z para la superficie
x = np.linspace(a, b, N + 1)
y = np.linspace(c, d, M + 1)
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
plt.show()
