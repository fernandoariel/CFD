import numpy as np
import matplotlib.pyplot as plt


N = 100 #numero de nodos
dt = 0.001 #paso del tiempo
L = float(1) #longitud de la grilla
nsteps = 60 #numero de pasos de tiempo
dx = L/(N-1) #espaciado de la grilla
a0=1
cfl=abs((a0*dt)/dx)
u=np.zeros(N)
x=np.linspace(0,1,N)

for i in range(N):
    if x[i]<=0.3:
        u[i]=1
    else:
        u[i]=0

for j in range(nsteps):
    u[1:-1] = (u[:-2] + u[2:]) / 2.0 - cfl * (u[2:] - u[:-2]) / 2.0


plt.plot(x,u)
plt.title('Lax Friedrichs')
plt.xlabel('X')
plt.ylabel(r'$\phi$')


plt.show()
print(cfl)
