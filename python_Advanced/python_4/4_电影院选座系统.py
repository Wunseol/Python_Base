row=5
col=8
seatSet=set(range(row*col))
while True:
    for i in range(row):
        for j in range(col):
            if i*col+j not in seatSet:
                print("%2s"%('X'), end=" ")
            else:
                print("%02d"%(i*col+j),end=" ")
        print('\n')
    tmp=input("\n请输入您要选择的座位,如果涉及多个请用逗号分隔\n")
    for t in tmp.split(","):
        seatSet.remove(int(t))