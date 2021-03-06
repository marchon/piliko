from fractions import Fraction

##########
##########
#
# rational parameterization of the unit sphere
#
#########
#########

# consider a basic unit sphere
#
# x^2 + y^2 + z^2 = radius = 1^2
#
#   x^2 + y^2 = l^2
#   l^2 + z^2 = radius^2
#   radius = 1, radius^2=1
#
# example: begin with very simple pythagorean triple numbers:, 3,4,5 and 5,12,13
#          now, assume x=3, y=4, l=5, z=12, radius=13. divide all by 13
#
#          x=3/13, y=4/13, l=5/13, z=12/13, radius=13/13=1
#
# to verify: , 3^2=9 4^2=16, 5^2=25, 12^2=144, 13^2=169  
# (3/13)^2+(4/13)^2+(12/13)^2 = (13/13)^2     [ qx+qy+qz=r=1 ]
# (3/13)^2+(4/13)^2 = (5/13)^2                [ qx+qy = ql   ]
# (5/13)^2+(12/13)^2 = (13/13)^2              [ ql+qz = qr=1 ]
#                                               qn = quadrance(n) = n^2
#
# therefore the given point, with x,y,z coordinates [ 3/13, 4/13, 12/13 ] is 
# a rational point on the unit sphere.

# theory
#
# Use the rational paramterization of the unit circle to find l and z. 
# 
# l = m^2-n^2 / m^2+n^2     z = 2*m*n / m^2+n^2
#
# now, note that x^2 + y^2 = l^2. 
# divide this equation by l^2, you get this:
#  (x/l)^2 + (y/l)^2 = 1
# 
# we can again use the rational paramterization of a unit circle but
# our "x" will actually be x/l and "y" will be y/l. We are using different
# m and n as well, call them "m1" and "n1" here. 
#
# x/l = m1^2-n1^2 / m1^2+n1^2     y/l = 2*m1*n1 / m1^2+n1^2
#
# Now. That is quite interesting. You can choose m1, n1 as integers and get
# values for x/l and y/l. But what if you want just x or y by itself?
#
# Ahh, remember, we calculated l up above, based on two other integers, m and n
# you can multiple the equations above by l to get your sol'n for x and y. 
#
# x = l * ( m1^2-n1^2 / m1^2+n1^2 )      y  = l * ( 2*m1*n1 / m1^2+n1^2 )
#
# you can use Algebra to rearrange all this, but basically, in the end, 
# we have x, y, and z as functions of m, n, m1, and n1, four separate integers.
#
#
# possible problem: i have no idea if this works. 
#
# and others have probably found better.

xs,ys,zs=[],[],[]
def sqr(x): return x*x
def blueq(x,y): return sqr(x)+sqr(y)
def redq(x,y): return sqr(x)-sqr(y)
def greenq(x,y): return 2*x*y
depth=8
for m in range(0,depth):
	for n in range(0,depth):
		for m1 in range(0,depth):
			for n1 in range(0,depth):
				if blueq(m1,n1)==0: continue
				if blueq(m,n)==0: continue
				if blueq(m1,n1)==0: continue
				l = Fraction( redq(m,n) , blueq(m,n) )
				z = Fraction( greenq(m,n) , blueq(m,n) )
				x = l * Fraction( redq(m1,n1), blueq(m1,n1) )
				y = l * Fraction( greenq(m1,n1), blueq(m1,n1) )
				print x,y,z,' sq sum: ',x*x+y*y+z*z
				xs += [x]
				ys += [y]
				xs += [y]
				ys += [x]
				zs += [z]
				zs += [-z]

print len(xs)
import numpy as np
import matplotlib.pylab as plt
fig,ax = plt.subplots(figsize=(8,8))

ax.set_ylim([-1.2,1.2])
ax.set_xlim([-1.2,1.2])
for i in range(0,len(xs)):
	xs[i]=xs[i]+zs[i]/4
	ys[i]=ys[i]+zs[i]/4
ax.scatter(xs,ys)
plt.show()

