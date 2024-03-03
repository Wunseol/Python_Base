# Python并没有对私有成员提供严格的访问保护机制。
# 在定义类的成员时，如果成员名以两个下划线“__”或更多下划线开头而不以两个或更多下划线结束则表示是私有成员。
# 私有成员在类的外部不能直接访问，需要通过调用对象的公开成员方法来访问，也可以通过Python支持的特殊方式来访问。
# 公开成员既可以在类的内部进行访问，也可以在外部程序中使用。


class A:
    def __init__(self, value1=0, value2=0):
        self.value1 = value1
        self.__value2 = value2
    def setValue(self, value1, value2):
        self.value1 = value1
        self.__value2 = value2
    def show(self):
        print(self.value1)
        print(self.__value2)

a = A()
print(a.value1)
# 0
print(a._A__value2)             #在外部访问对象的私有数据成员
# 0


# 在Python中，以下划线开头的变量名和方法名有特殊的含义，尤其是在类的定义中。
# __xxx__：系统定义的特殊成员；
# __xxx：私有成员，只有类对象自己能访问，子类对象不能直接访问到这个成员，但在对象外部可以通过“对象名._类名__xxx”这样的特殊方式来访问。
# 注意：Python中不存在严格意义上的私有成员。

