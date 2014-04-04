#!/usr/bin/python
from numpy import *
import pylab as lab

n, dt = 200, 0.5
x,y = meshgrid(arange(n,dtype=float32)/n, arange(n,dtype=float32)/n)
u = exp(-((x-0.2)*20.)**2 -((y-0.3)*20.)**2)
v = zeros((n,n), dtype=float32)
lab.ion()
image = lab.imshow(u, cmap='cool')

for i in range(100000):
	v[1:-1,1:-1] -= (4.*u[1:-1,1:-1]-u[:-2,1:-1]-
	u[2:,1:-1]-u[1:-1,:-2]-u[1:-1,2:])*dt
	u[1:-1,1:-1] += v[1:-1,1:-1] * dt
	if i % 10 == 0:
		image.set_data(u)
		image.autoscale()
		lab.draw()
