import random
count=1
red=set()
blue=set()

print("红球:")
while count<=6:
    num1=random.randint(1,33)
    red.add(num1)
    count+=1  
print(red)      

print("蓝球:")
blue=random.randint(1,16)
print(blue)

print("双色:")
double=list(red)
double.append(blue)
print(double)

