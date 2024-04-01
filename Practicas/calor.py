import numpy as np
import matplotlib.pyplot as plt

#Tipo de ecuación:
#du/dt = alpha * d^2u/dx^2 

#Determinamos nuestra región R:

a = 0
b = 15 #Longitud de la barra
c = 0
d = 5

#Determinamos el número de subdivisiones

M = 400
N = 40

#Determinamos los pasos

h = b/N
k = d/M

#Determinamos la conductividad térmica



#Determinamos la matriz w

w = np.zeros((M+1, N+1))

#Determinamos las funciones:

def f(x):
    return np.exp(-(x-b/2)**2)

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
    w[1][i] = w[0][i] + k * g(i * h)

alpha = 1/(1-i*h)

#Aplicamos diferencias finitas

for j in range (1, M):
    for i in range(1,N):
        w[j+1][i] = k*alpha/h**2*(w[j][i+1] - 2*w[j][i] + w[j][i-1]) + w[j][i]

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
