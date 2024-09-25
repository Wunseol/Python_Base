import math

a=0
b=10
count1=1

def m(num1,num2):
    print((num1+num2)/2)
    return (num1+num2)/2

def f(x):
    y=math.pow(x,2)-x-1
    print(y)
    return y

num_a=f(a)
num_b=f(b)
num_m=m(a,b)

while count1<100:
    if num_a<0 and num_m>0:
        num_a=f(a)
        num_b=f(b)
        num_m=m(a,b)
        print("解的范围[0,m]=[0,%f]"%num_m)
        if num_m<0.00001:
            break
        b=num_m
    count1+=1






