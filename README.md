piliko
======

Piliko is a very, very, very basic implementation of some formulas from 
Rational Trigonmetry in a computer language. 

This package is not affiliated with, nor endorsed in any way by Norman J 
Wildberger, who created Rational Trigonometry. For more info, check these
websites:

https://www.youtube.com/user/njwildberger

http://web.maths.unsw.edu.au/~norman/

http://www.wildegg.com

http://www.cut-the-knot.org/pythagoras/RationalTrig/CutTheKnot.shtml

http://farside.ph.utexas.edu/euclid.html

The language used is Python, but using features where we break lots of 
conventions (use of *args and object inspection).

Current status
==============

alpha level, currently does very little and/or nothing. 

Examples
========

Basic usage:

     # note ---> we use the line equation ax+by+c = 0
     from piliko import *
     L1 = line(1,-2,3) 
     L2 = line(4,-3,7)
     s = spread(L1,L2)
     print L1, L2, s

Result:

     <1:-2:3> <4:-3:7> 1/5

More examples can be found in test.py. To run it:

     python test.py



Copyright License
=================

This code is free for use under a basic BSD-style Open Source Software 
license as described in the LICENSE file.
