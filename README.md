piliko
======

Piliko is a very, very, very basic implementation of some formulas from 
the Rational Trigonmetry and Rational Geometry as described by Norman J 
Wildberger. This package is not affiliated in any way with Norman J 
Wildberger.

Current status
==============

alpha level, currently does very little and/or nothing. 

Examples
========

Basic usage:

     from piliko import *
     l0 = line(1,-2,3)       # ax+by+c = 0 is the line equation
     l1 = line(4,-3,7)
     s = spread(l0,l1)
     print l0, l1, s

Result:

     <1:-2:3> <4:-3:7> 1/5

More examples can be found in test.py. To run it:

     python test.py









