# 6.小明购买了一张 08-16 19:40 三亚->上海的机票，机票价格为2870元，然后190元，机建50元，保险40元，
# 因疫情影响，需要进行退票操作，请计算退票金额。
# 退票规则:
# 航班规定离站时间72小时(含)之前，每次收取实际票面价10%的退票手续费;
# 航班规定离站时间前72小时(不含)至航班规定离站时间前4小时(含)，每次收取实际票面价20%的退票手续费;
# 航班规定离站时间前4小时(不含)至航班起飞后，每次收取实际票面价40%的退票手续费。(婴儿免收退票费)

import datetime

take_off_date = datetime.datetime.strptime('2022-8-16 19-40-0','%Y-%m-%d %H-%M-%S')
now=datetime.datetime.today()
delta=take_off_date-now
day=delta.days
hour=int(delta.seconds/60/60)
minute=int((delta.seconds-hour*60*60)/60)
second=delta.seconds-hour*60*60-minute*60
print("距 2022-8-16 19-40-0 还有"+str(day)+'天'+str(hour)+'时'+str(minute)+'分'+str(second)+'秒')
print("距航班规定离站的时间为(参考):"+str(hour+day*24)+'时'+str(minute)+'分'+str(second)+'秒')

money_1 = int(input("实际票面价格:"))
money_2 = int(input("其它费用:"))
n = int(input("距航班规定离站的时间（小时）：")) 
flag = int(input("是否为婴儿(是则输入1,否则输入0):"))
if flag==0 :
    if n>=72:
        m=money_1-money_1*0.1+money_2
        print("退票费用为:",money_1*0.1)
        print("退总金额为:",m)
    elif n>=4:
        m=money_1-money_1*0.2+money_2
        print("退票费用为:",money_1*0.2)
        print("退总金额为:",m)
    elif n<4:
        m=money_1-money_1*0.4+money_2
        print("退票费用为:",money_1*0.4)
        print("退总金额为:",m)
else :
    m=money_1+money_2
    print("退票费用为:",0)
    print("退总金额为:",m)
