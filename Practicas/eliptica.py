import numpy as np
import matplotlib.pyplot as plt

# No es un problema de evolución --> se aplica el método de Gauss-Seidel

a = 0
b = 1 #Longitud de la barra
c = 0
d = 1

#Determinamos el número de subdivisiones

M = 30
N = 30

#Determinamos los pasos

h = b/N
k = d/M

#Determinamos la matriz w

w = np.zeros((M+1, N+1))

#Determinamos las funciones:

#f(x) determina el valor de u en t=0

def f(x):
    return np.exp(-(x-0.25)**2)

#g(x) determina el valor de la derivada de u en t=0

def g(x):
    return 0

#Notación de x, t:
#x = h*i
#t = k*i

#Determinamos las condiciones de contorno
#u(i, t)

for j in range(1, M):
    w[j][0] = 0
    w[j][N] = 0

#u(x, j)

for i in range(1, N):
    w[0][i] = f(i * h) 
    w[1][i] = 0

#Aplicamos Gauss-Seidel

for p in range(100):
    for j in range (1, M):
        for i in range(1,N):
            w[j][i] = (4 * k**2 * (w[j][i+1] + w[j][i-1]) + h * k * (w[j+1][i+1] + w[j-1][i-1] - w[j+1][i-1] - w[j-1][i+1]) + 4 * h**2 * (w[j+1][i] + w[j-1][i]))/(8 * (h**2 + k**2))


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

#plt.savefig('img/Ondas.png')

plt.show()