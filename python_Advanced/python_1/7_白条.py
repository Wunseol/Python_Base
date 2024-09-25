# 7.小明准备在京东上买1台价值4799的笔记本，现有2张优惠券，满3000-50或白条6期免息付款。请问那种方式更划算？ 
i=1
x=6
sum=0
money=float (input("自己的钱："))
# flag=int (input("方法: 1 or 2 :"))
# if flag == 1 :
if money>=3000 :    #and money<6000: 
    print("方法1省了",50)
    # elif money>=6000:
    #     less1=100
# elif flag == 2 :
for i in range(x) :
    sum=sum+money*0.0001*30  
    # print(sum)
    money=money-money/6
    # print(money)
print("方法2省了",sum)

