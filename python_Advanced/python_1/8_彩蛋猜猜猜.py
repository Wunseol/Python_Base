import random
num=random.randint(500,3072)
max=3072
min=500
count=1

third =(num-1000*(num//1000))//100
print("___%d___ ___\n\n"%third)

if third<=4:
    min=1000+third*100
else:
    min=third*100
if third !=0:
    max=2099+third*100
while 1:
    print("当前范围%d,%d"%(min,max))
    t=input("%d请输入您的手机号:"%count)
    guess=int (input("请输入您的猜测："))

    if num>guess:
        print("%d猜小了\n\n"%guess)
        if guess>min:
            min=guess       
    elif num<guess:
        print("%d猜大了"%guess)
        if guess<max:
            max=guess
    elif num==guess:
        if count==1:
            print("第一个人获得%dMB"%num)
        else:
            print("第一个人获得%dMB"%(num/2))
            i=2
            while i<count:
                print("第%d个人获得%dMB"%(i,num/4/(count-2)))
                i+=1
            print("第%d个人获得%dMB"%(count,num/4))    
        break
    count+=1