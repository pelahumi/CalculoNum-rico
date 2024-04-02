import numpy as np
import matplotlib.pyplot as plt

#Tipo de ecuación:
#du/dt = alpha * d^2u/dx^2 

#Determinamos nuestra región R:

a = 0
b = 5 #Longitud de la barra
c = 0
d = 10

#Determinamos el número de subdivisiones

M = 400
N = 40

#Determinamos los pasos

h = b/N
k = d/M

#Determinamos la conductividad térmica

v = 0.5

#Determinamos la matriz w

w = np.zeros((M+1, N+1))

#Determinamos las funciones:

#f(x) determina el valor de u en t=0

def f(x):
    return np.exp(-(x-2.5)**2)

#g(x) determina el valor de la derivada de u en t=0

def g(x):
    return 0

#Notación de x, t:
#x = h*i
#t = k*i

#Determinamos las condiciones de contorno
# Como es un problema de evolución, no se da un dato de contorno que limite el tiempo
#u(i, t)

for j in range(1, M):
    w[j][0] = 0
    w[j][N] = 0

#u(x, j)

for i in range(1, N):
    w[0][i] = f(i * h) 
    w[1][i] = w[0][i] + k * g(i * h)



#Aplicamos diferencias finitas
#Método de evolución temporal (diferencias progresivas)

for p in range(100):
    for j in range (1, M):
        for i in range(1,N):
            w[j][i] = (k*(w[j][i+1] + w[j][i-1]) + h**2 * (1 + i*h) * w[j-1][i]) / (2 * k + h**2 * (1 + h*i) - (1 + h*i) * h**2 * k)

#Si usamos diferencias regresivas, es necesario iterar usando Gauss-Seidel (deja de ser un problema de evolución) y se despeja el término    w[j][i]

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
