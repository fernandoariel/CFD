import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags

N = 8##numero de nodos
dt = 1 #time step
L = float(1) #longitud de la grilla
nsteps = 100#numero de pasos de tiempo
dx = L/(N-1) #espaciado de la grilla

r =(0.0001*dt)/(2*dx**2) # coeficiente Delta

A = diags([-r, 1+2*r, -r], [-1, 0, 1], shape=(N-2, N-2)).toarray() #creo matriz A
B=diags([r, 1-2*r, r], [-1, 0, 1], shape=(N-2, N-2)).toarray()  #creo matriz B
b=np.zeros((N-2)) #vector de BC's
b[0]=100
b[-1]=100
#creo la grilla y Ic's
x=np.linspace(0,1,N)
u=np.zeros(N)
u[0]=100
u[-1]=100
#evaluo el lado derecho de la ecuacion en t=0 [B]*u(n)+b
bb = B.dot(u[1:-1])+2*r*b

Vout=np.zeros(N)

for j in range(nsteps):
    # solucion
    u[1:-1] = np.linalg.solve(A, bb)
    # actualizo valores de bb
    bb = B.dot(u[1:-1]) +2*r*b

Vout=u.copy()

plt.plot(x, u,label='%.d Nodos'%N)
plt.title('Crank-Nicolson')
plt.xlabel('X')
plt.ylabel(r'$\phi$')

plt.legend()
plt.savefig('Crank.png')
plt.show()
print(Vout)


