import matplotlib.pyplot as plt
import numpy as np

def verlet(xt,vt):
	p=xt+vt*dt+0.5*(-xt*(k/m)-(np.sign(vt)*fat))*dt**2
	f=vt+0.5*((-p*(k/m)-(np.sign(vt)*fat))+(-xt*(k/m)-(np.sign(vt)*fat)))*dt
	return p,f

mi=0.003
m=1
k=1
g=9.8
n=m*g
fat=mi*n
dt=0.001
t=[0]
xt1=1
vt1=0
t1=0
x=[1]
v=[0]

while t1<55:
	t1+=dt
	xt1,vt1=verlet(xt1,vt1)
	x.append(xt1)
	v.append(vt1)
	t.append(t1)

plt.figure(figsize=(6,5), dpi=96)

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'Posi\c{c}\~{a}o(m)')
plt.ylabel(r'Velocidade($\frac{m}{s}$)')

plt.title(r'Oscila\c{c}\~{a}o Com Atrito Espa\c{c}o de Fases', fontsize=12)
plt.grid()
plt.plot(x,v, 'r-', linewidth=1)
plt.savefig("XxV.pdf", dpi=96)
plt.show()
