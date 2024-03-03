# Python类有大量的特殊方法，其中比较常见的是构造函数和析构函数，除此之外，Python还支持大量的特殊方法，运算符重载就是通过重写特殊方法实现的。
# Python中类的构造函数是__init__()，一般用来为数据成员设置初值或进行其他必要的初始化工作，在创建对象时被自动调用和执行。如果用户没有设计构造函数，Python将提供一个默认的构造函数用来进行必要的初始化工作。
# Python中类的析构函数是__del__()，一般用来释放对象占用的资源，在Python删除对象和收回对象空间时被自动调用和执行。如果用户没有编写析构函数，Python将提供一个默认的析构函数进行必要的清理工作。
class Car :
    def __init__(self, n):
        self.num=n
        print(str(self.num))
    def __del__(self):
        print(str(self.num)+" is deleted")

car1=Car(1)
car2=Car(2)
del car1
del car2
