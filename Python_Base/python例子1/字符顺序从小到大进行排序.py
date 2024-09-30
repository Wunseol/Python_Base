# -*- coding: UTF-8 -*-

# 程序从键盘输入一个字符串（长度不超过80），然后用选择法按照字符顺序从小到大进行排序，最后输出排序后的字符串。

# str=list(input("Please enter a string:"))
# if len(str)>80:
#     print("error!")
# else:
#     str.sort() 
#     str="".join(str) 
#     print("The sorted string is:%s"%str)

# 从用户输入中获取一个字符串并将其转换为列表
str = list(input("请输入一个字符串:"))

# 如果字符串的长度大于80，则输出错误信息
if len(str) > 80:
    print("错误！")
else:
    # 对字符串列表进行排序
    str.sort()
    # 将排序后的列表转换为字符串
    str = "".join(str)
    # 输出排序后的字符串
    print("排序后的字符串为：%s" % str)




