
list1=["柳" , "唐" , "颜" ,"慕容" , "叶" , "沈" , "杜" , "凌" , "花" , "莫" ]
list2=["蓝","芊" ,"碧" ," " ,"双" ,"吟"  ,"玉","琪" ,"竹" ,"香"  ,"依" ,"若" ]
list3=[" ","月","雪","晨","宁","萍","落","楹","秋","溪"," ","芊"," ","涵","依","点","双","蓉"," ","惠","婷","佳"," ","萱","思","薇","儿","韵"," ","菲","乐"]

year=int(input("年:"))
month=int(input("月:"))
day=int(input("日:"))
print("你前世的名字是:",list1[year%10],list2[month],list3[day])
