# 在类中定义的方法可以粗略分为四大类：公有方法、私有方法、静态方法和类方法。
# 私有方法的名字以两个下划线“__”开始，每个对象都有自己的公有方法和私有方法，在这两类方法中可以访问属于类和对象的成员；
# 公有方法通过对象名直接调用，私有方法不能通过对象名直接调用，只能在属于对象的方法中通过self调用或在外部通过Python支持的特殊方式来调用。

# 静态方法属于类，静态方法可以通过类名调用。Python使用 @ staticmethod指令的方式将普通函数变成静态方法。
# 静态方法可以没有参数。
class Fruit:
    price=0
    def __init__(self):
            self.__color='Red'		 #定义设置私有属性color
            self.__city='Kunming'	 #定义和设置私有属性city
    def __outputColor(self):	 #定义私有方法outputColor
            print(self.__color)		 #访问私有属性color
    def __outputCity(self):	 #定义私有方法outputCity
            print(self.__city)	          #访问私有属性city

    def output(self):		#定义公有方法output
        self.__outputColor( )	#调用私有outputColor
        self.__outputCity( )	#调用私有outputCity
    @ staticmethod
    def getPrice():			#定义静态方法getPrice
         return Fruit.price
    @ staticmethod
    def setPrice(p):		#定义静态方法setPrice
        Fruit.price=p

apple=Fruit()
apple.output() 
print(Fruit.getPrice( ))
Fruit.setPrice(9)
print(Fruit.getPrice( ))
# apple.__outputColor( )   #输出结果报错

# self代表类的实例，而非类。
class Test:
    def prt(self):
        print(self)
        print(self.__class__)      #指向实例对应的类
t = Test()
t.prt()

# 执行结果如下：
# <__main__.Test object at 0x000000000284E080>
# <class '__main__.Test'>
# 从上面的例子中可以很明显的看出，self代表的是类的实例。而self.__class__则指向类。
