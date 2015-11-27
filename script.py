# demo for showing off modules

import mymods.coolclass as cc
import mymods.neatfunctions as nf

# cool class module
a = 5
b = 'bro'

c = cc.CoolClass(a, b)

print 'demoing print stuff function of cool class'
c.print_stuff()

print 'showing member variables of cool class'
c.x = 10
print c.x
print c.y

# functions module
g = 20
h = 40

print 'using just a bunch of functions from neat functions'
print 'adding:', nf.add(g, h)
print 'multiplying:', nf.multiply(g, h)


