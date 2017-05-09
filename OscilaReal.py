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
i=0

while t1<25:
	t1+=dt
	xt1,vt1=verlet(xt1,vt1)
	x.append(xt1)
	v.append(vt1)
	t.append(t1)
	if xt1>-0.001 and xt1<0.001:
		i+=1
		print "%d: x=%f, t=%f\n"%(i, xt1, t1)
