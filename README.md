piliko
======

Piliko is a very, very, very rough implementation of some formulas from 
Rational Trigonmetry in a computer language. 

Current status
==============

This code is 'alpha' level. It is highly experimental. It can do basic 
calculations, but the whole type system has not been thought out very 
carefully and many functions are partially or wholly unimplemented. 
Tests have not been created.

Disclaimer 
==========

This package is not affiliated with, nor endorsed in any way by Norman J 
Wildberger, who developed Rational Trigonometry. For more info, check these
websites:

* https://www.youtube.com/user/njwildberger
* http://web.maths.unsw.edu.au/~norman/
* http://www.wildegg.com
* http://www.cut-the-knot.org/pythagoras/RationalTrig/CutTheKnot.shtml
* http://farside.ph.utexas.edu/euclid.html

The computer language used is Python.


But I don't know the computer language Python
=============================================

You don't need to know Python to do basic calculations. The syntax is
designed to be somewhat simple. Please see the examples. As long as you can
start up a python interpreter on your machine, you should be OK. See
http://www.python.org to download a python interpreter for your computer. 
Once you can get to the screen where you type 
	
	print 'hello world'

then you will be ready to use piliko. Just put piliko.py in the proper
folder and you can load it with this command:

	from piliko import *

Examples
========

Example 1:

	from piliko import *

	p1 = point(0,0)
	p2 = point(3,0)
	p3 = point(0,4)
	print p1,p2,p3

	L1 = line( p1, p2 )
	L2 = line( p1, p3 )
	s = spread( L1, L2 )
	print s

Result:

	[0,0] [3,0] [0,4]
	1

Example 2:

	from piliko import *

	v1 = vector(3,0)
	v2 = vector(0,4)
	print v1, v2

	q1 = quadrance( v1 )
	q2 = quadrance( v2 )
	print q1, q2

	s = spread( v1, v2 )
	print s

Result:

	(3,0) (0,4)
	9 16
	1

Example 3:

	p1,p2,p3,p4 = point(0,0),point(3,0),point(2,0),point(6,0)
	print is_harmonic_range( p1, p2, p3, p4 )

Result:

	True

Example 4:

	p=point(3,4)
	bq,rq,gq=blue_quadrance(p),red_quadrance(p),green_quadrance(p)
	print p,' ',bq,rq,gq,' ',sqr(bq),sqr(rq),sqr(gq)

Result:

	[3,4]   25 -7 24   625 49 576

More examples can be found in test.py. To run it:

	python test.py

Basic principle
===============

The Rational numbers, unlike finite floating point numbers, are closed 
under addition, subtraction, multiplication, and division. This makes 
them uniquely suited to geometry, as many geometry packages have proven. 
Why? Because many of the basic geometry operations, including scale, 
translate, boolean, intersection, etc, are doable in algebra using only 
plus, minus, multiply, and divide. 

Therefore no approximation is required to perform these basic 
operations, which means the issue of floating-point error disappears.

In fact it is possible to develop a geometry that does not use 
transcendental functions at all. There are rational analogues for 
rotation. Any conic curve can be approximated very well by rational 
parameterization (rational points on the curve). Bezier curves can be 
approximated by rational points. And thus, truetype fonts. Also a large 
number of polynomial curves can be parameterized by rational points. 
There are even people working algorithms to create rational 
paramterizations automatically.

By 'approximate' here I mean not just 'pretty close', I mean 'to an arbitrary
precision', which means that the approximations will be just as good as 
if we used cosine, sine, etc, to get decimal approximations. The difference
is that with a rational approximation, we dont lose information when we
rotate, scale, etc. With decimal approx, you cant even do "shrink it by 
1/3" without losing information. 

It may be even possible to create anlogues of geometry algorithms (like 
catmull clark subdivision) using rational points and rational functions.

The downside is that you lose some old things, like the notion of distance,
or the intersection of any line with any circle. Even the length of the
side of a 45-45-90 triangle is lost. 

Another huge loss is that you can't add two angles together with simple 
addition. You have to use 'spread polynomials' which are immensly 
complicated compared to addition.

The other downside is it's slow. Computers were optimized for floating 
point for 50 years. Hardware doesnt generally deal with rationals. You 
also have to worry about overflowing your integers. Typically rational 
number software uses 'big int', which can expand the integer past the 
size native to the machine. For example on a 32-bit computer 'big int' 
allows the use of integers larger than the maximum expressable in 32 
bits, which is around ~4 billion. This makes it slow though.

Copyright License
=================

This code is free for use under a basic BSD-style Open Source Software 
license as described in the LICENSE file.
