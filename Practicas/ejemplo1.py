import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 5
c = 0
d = 10

M = 400
N = 40

h = (b - a) / N
k = (d - c) / M

w = np.zeros((M+1, N+1))

def f(x):
    return np.exp(-(x-2.5)**2)

def g(x):
    return 0

# Aquí introducimos los datos de contorno
for j in range(1, M):
    w[j][0] = 0
    w[j][N] = 0

for i in range(1, N):
    w[0][i] = f(i * h) 
    w[1][i] = w[0][i] + k * g(i * h)

for p in range(100):
    for j in range (1, M):
        for i in range(1,N):
            w[j][i] = (k*(w[j][i+1] + w[j][i-1]) + h**2 * (1 + i*h) * w[j-1][i]) / (2 * k + h**2 * (1 + h*i) - (1 + h*i) * h**2 * k)

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

