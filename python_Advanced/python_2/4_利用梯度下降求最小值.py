import math

eta=0.3

x=0

for i in range(10):
    x=x-eta*(2*x-2)
    print("x_%d=%.4f"%(i+1,x))
f_min=x*x-2*x+6
print("f_min=%.4f"%f_min)

