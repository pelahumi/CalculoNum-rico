import numpy as np
import matplotlib.pyplot as plt

#Tipo de ecuación:
#du/dt = alpha * d^2u/dx^2 

#Determinamos nuestra región R:

a = 0
b =  #Longitud de la barra
c = 0
d = 

#Determinamos el número de subdivisiones

M = 
N = 

#Determinamos los pasos

h = b/M
k = d/N

#Determinamos la conductividad térmica

alpha = 

#Determinamos la matriz w

w = [[0 for i in range(N + 1)] for j in range(M + 1)]

#Determinamos las funciones:

def f(x):
    return 0

def g(x):
    return 0

#Notación de x, t:
#x = h*i
#t = k*i

#Determinamos las condiciones de contorno
#u(i, y)

for j in range(1, M):
    w[j][0] = 0
    w[j][N] = 0

#u(x, j)

for i in range(1, N):
    w[0][i] = f(i * h) 
    w[1][i] = w[0][i] + k * g(i * h)

#Aplicamos diferencias finitas

for j in range (1, M):
    for i in range(1,N):
        w[j+1][i] = (1 - (2 * k * alpha**2)/h**2) * w[j][i] + (k * alpha**2) / h**2 * (w[j][i+1] + w[j][i-1])

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
