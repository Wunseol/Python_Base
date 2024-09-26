import math
import numpy

i = 0
for x in numpy.arange(0.00,1.00,0.01):
    i=i+(x+5)/(x*x-6*x+13)
print(i/100)