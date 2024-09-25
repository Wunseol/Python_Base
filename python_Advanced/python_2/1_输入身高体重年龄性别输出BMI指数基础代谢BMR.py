import math

h=float(input("高:(cm)"))
w=float(input("重:(kg)"))
age=int(input("年龄:(year)"))
s=int(input("男填1女填2:"))
if s==1 :
    print("你的BMI为:%f"%(w/pow(h/100,2)))
    print("你的BMR为:%f"%((13.7*w)+(5.0*h)-(6.8*age)+66))
elif s==2:
    print("你的BMI为:%f"%(w/pow(h/100,2)))
    print("你的BMR为:%f"%((9.6*w)+(1.8*h)-(4.7*age)+655))
else :
    print("error")


