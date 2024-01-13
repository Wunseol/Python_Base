x = 1235
"%o" % x
# "2323"
"%x" % x
# "4d3"
"%e" % x
# "1.235000e+03"
"%s" % 65
# "65"
"%s" % 65333
# "65333"
'%s'%[1, 2, 3]        #直接把对象转换成字符串
# '[1, 2, 3]'

# Python提供了一种输出格式化字符串的函数，即string.format()函数，string是预输出的字符串。format()函数可以通过“{}”和“:”输出各种格式的字符串。“{}”指定了字符串中使用数据的序号，按照序号用对应的数据代替。若没有提供数据序号，则按照先后顺序依次提供。

print("2018年，你选修了5门课程！")
# 2018年，你选修了5门课程！
a=2019
b=6
print(a,"年，你选修了”,b,“门课程！")
# 2019年，你选修了6门课程！
print("{}年，你选修了{}门课程！".format(a,b))
# 2019年，你选修了6门课程！
print("{}年，你选修了{}门课程！".format("2019",6))


print('{0},{1}'.format('carmen',20))
# carmen,20
print('{},{}'.format('carmen',20))
# carmen,20
print('{1},{0},{1}'.format('carmen',20))
# 20,carmen,20
print('{name},{age}'.format(age=20,name='carmen'))
# carmen,20

# 使用format方法进行格式化
print("The number {0:,} in hex is: {0:#x}, the number {1} in oct is {1:#o}".format(5555,55))
# The number 5,555 in hex is: 0x15b3, the number 55 in oct is 0o67
print("The number {1:,} in hex is: {1:#x}, the number {0} in oct is {0:o}".format(5555,55))
# The number 55 in hex is: 0x37, the number 5555 in oct is 12663
print("my name is {name}, my age is {age}, and my QQ is {qq}".format(name="Dong Fuguo",age=40,qq="30646****"))
# my name is Dong Fuguo, my age is 40, and my QQ is 30646****
position = (5, 8, 13)
print("X:{0[0]};Y:{0[1]};Z:{0[2]}".format(position))
# X:5;Y:8;Z:13
'{0:<8d},{0:^8d},{0:>8d}'.format(65) #设置对齐方式
# '65      ,   65   ,      65
'{0:+<8d},{0:-^8d},{0:=>8d}'.format(65)
# '65++++++,---65---,======65'

weather = [("Monday","rainy"),("Tuesday","sunny"),
           ("Wednesday", "sunny"),("Thursday","rainy"),
           ("Friday","cloudy")]
formatter = "Weather of '{0[0]}' is '{0[1]}'".format
for item in map(formatter,weather):
    print(item)
for item in weather:
    print(formatter(item))
# 运行结果：
# Weather of 'Monday' is 'rainy'
# Weather of 'Tuesday' is 'sunny'
# Weather of 'Wednesday' is 'sunny'
# Weather of 'Thursday' is 'rainy'
# Weather of 'Friday' is 'cloudy'


