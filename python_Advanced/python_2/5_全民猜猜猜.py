# 5.	模拟“全民猜猜猜”小游戏
# 一、活动规则
# a)	1、活动期间，客户每天可参与一次游戏，活动期间仅限三次;
# b)	客户进入游戏，和教授会随机分配给出您要玩要的地点和事件，您可以马上参与竞猜:如客户自己猜中游戏的地点和事件，则可获得游戏100%的流量;
# c)	如发起游戏的用户自己未猜中，可将游戏告诉给其他好友竞猜，游戏被猜中，则游戏所含流量的50%归屋于发起游戏的客户，25%归尾于猜中游戏的客户，剩余25%被其他参与竞猜的客户平分，如游戏第一次就被好友猜中，则猜中的好友可获得50%的流量。
# d)	活动期间同一个游戏，每位客户仅可竞猜一次。
# e)	活动流量将于游戏被猜中后发放，舍去小数点后数字精确到1MB，用户需要进入活动页面“玩耍记录”自行领取;
# 二、奖项设置
# a)	1、每个游戏含有200M上海移动超套本地数据流量礼包;
# b)	2、游戏流量领取后24小时内到账，为上海移动超套本地数据流量(可于套餐内流量用尽后抵扣上海本地2/34G网络下产生的流量)，当月使用有效，过期作废;
# c)	3、活动流量到账需客户手机正常使用未出现停机、欠费等状态，且已开通移动数据功能。
# d)	4、活动期间用户未及时领取流量，活动结束后不补赠。返回


import random
place=random.randint(0,11)
time=random.randint(0,11)
count=1
num=200
print(place)
print(time)

list1=["酒店" , "KTV" , "博物馆" ,"酒吧" , "奶茶店" , "铁轨上" , "床上" , "小树林里" , "人群中" , "小船上" , "公共厕所" , "烤鸭店前" ]
list2=["吹萨克斯" , "游泳" , "吃泡面" ,"唱歌" , "跳广场舞" , "敷面膜" , "吃鸡" , "数钱" , "刮腿毛" , "洗澡" , "吃臭豆腐" , "看日出" ]

def menu():
    print("\n")

    # for i in range(11):
    #     print(i,list1[i])
  
    # print("\n")

    # for i in range(11):
    #     print(i,list2[i])

    print("--------------------------地点---------------------------\n")
    print("0.酒店           1.KTV           2.博物馆\n")
    print("3.酒吧           4.奶茶店         5.铁轨上\n")
    print("6.床上           7.小树林里       8.人群中\n")
    print("9.小船上         10.公共厕所      11.烤鸭店前\n")

    print("--------------------------时间---------------------------\n")
    print("0.吹萨克斯       1.游泳            2.吃泡面\n")
    print("3.唱歌           4.跳广场舞        5.敷面膜\n")
    print("6.吃鸡           7.数钱            8.刮腿毛\n")
    print("9.洗澡           10.吃臭豆腐       11.看日出\n")

    print("\n")
    print("周请你帮忙一起猜猜:\n")
    print("我到底在哪里干什么?\n")
    
menu()

while 1:
    n=int(input("请输入地址编号:"))
    m=int(input("请输入地址编号:"))
    if n==place and m==time:
        print("正确")
        if count==1:
            print("第1个人获得%dMB"%num)
        else:
            print("第1个人获得%dMB"%(num/2))
            i=2
            while i<count:
                print("第%d个人获得%dMB"%(i,num/4/(count-2)))
                i+=1
            print("第%d个人获得%dMB"%(count,num/4))    
        break

    else:
        print(list1[n],list2[m])
        print("不正确")
    count+=1
