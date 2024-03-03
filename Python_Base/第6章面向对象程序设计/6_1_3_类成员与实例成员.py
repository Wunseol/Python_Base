# 属于实例的数据成员一般是指在构造函数__init__()中定义的，定义和使用时必须以self作为前缀；属于类的数据成员是在类中所有方法之外定义的。
# 在主程序中（或类的外部），实例属性属于实例(对象)，只能通过对象名访问；而类属性属于类，可以通过类名或对象名都可以访问。
# 在实例方法中可以调用该实例的其他方法，也可以访问类属性以及实例属性。

# 在Python中，可以动态地为自定义类和对象增加或删除成员，这一点是和很多面向对象程序设计语言不同的，也是Python动态类型特点的一种重要体现。

class Car:
    price = 100000                     #定义类属性
    def __init__(self, c):
        self.color = c                 #定义实例属性

car1 = Car("Red")                      #实例化对象
car2 = Car("Blue")
print(car1.color, Car.price)           #查看实例属性和类属性的值
Car.price = 110000                     #修改类属性
Car.name = 'QQ'                        #动态增加类属性
car1.color = "Yellow"                  #修改实例属性
print(car2.color, Car.price, Car.name)
print(car1.color, Car.price, Car.name)

# 在Python中，函数和方法是有区别的。方法一般指与特定实例绑定的函数，通过对象调用方法时，对象本身将被作为第一个参数隐式传递过去，普通函数并不具备这个特点。




