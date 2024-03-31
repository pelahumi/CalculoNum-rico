import numpy as np
import matplotlib.pyplot as plt

#Tipo de ecuación:
#d^2u/dx^2 - 1/v^2 * d^2u/dt^2 

#Determinamos nuestra región R:
#En ondas a y c suelen ser 0

a = 0
b = 6
c = 0
d = 24

#Determinamos el número de intervalos

M = 2400
N = 600
h = (b-a)/N
k = (d-c)/M

#Determinamos p y la velocidad de propagación

v =0.5
p = v*k/h

#Determinamos la matriz w

w = [[0 for i in range(N + 1)] for j in range(M + 1)]

#Notación de x, y:
#x = h*i
#y = k*i

#Determinamos las funciones:

def f(x):
    return 0

def g(x):
    return 0

#Determinamos las condiciones de contorno
#u(i, y)

for j in range(1, M):
    w[j][0] = 3*np.cos(k*j)
    w[j][N] = 0

#u(x, j)

for i in range(1, N):
    w[0][i] = f(i * h) 
    w[1][i] = w[0][i] + k * g(i * h)

#Aplicamos diferencias finitas

for j in range (1, M):
    for i in range(1,N):
        w[j+1][i] = 2*(1 - p**2)*w[j][i] + (p**2)*(w[j][i+1] + w[j][i-1]) - w[j-1][i]

#Dibujamos

x = np.linspace(a, b, N+1)
y = np.linspace(c, d, M+1)
x, y = np.meshgrid(x, y)
z = np.array(w)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('t')
ax.set_zlabel('Z')
ax.set_title('Superficie 3D')

#plt.savefig('img/Ondas.png')

plt.show()
