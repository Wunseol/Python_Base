# 面向对象程序设计
# 面向对象程序设计（Object Oriented Programming，OOP）主要针对大型软件设计而提出，使得软件设计更加灵活，能够很好地支持代码复用和设计复用，并且使得代码具有更好的可读性和可扩展性。
# 面向对象程序设计的一条基本原则是计算机程序由多个能够起到子程序作用的单元或对象组合而成，大大地降低了软件开发的难度。
# 面向对象程序设计的一个关键性观念是将数据以及对数据的操作封装在一起，组成一个相互依存、不可分割的整体，即对象。对于相同类型的对象进行分类、抽象后，得出共同的特征而形成了类，面向对象程序设计的关键就是如何合理地定义和组织这些类以及类之间的关系。
# Python完全采用了面向对象程序设计的思想，是真正面向对象的高级动态编程语言，完全支持面向对象的基本功能，如封装、继承、多态以及对基类方法的覆盖或重写。
# Python中对象的概念很广泛，Python中的一切内容都可以称为对象，除了数字、字符串、列表、元组、字典、集合、range对象、zip对象等等，函数也是对象，类也是对象。
# 创建类时用变量形式表示的对象属性称为数据成员，用函数形式表示的对象行为称为成员方法，成员属性和成员方法统称为类的成员。


# Python使用class关键字来定义类，class关键字之后是一个空格，然后是类的名字，再然后是一个冒号，最后换行并定义类的内部实现。
# 类名的首字母一般要大写，当然也可以按照自己的习惯定义类名，但一般推荐参考惯例来命名，并在整个系统的设计和实现中保持风格一致，这一点对于团队合作尤其重要。

class Car: 
    def infor(self):
        print(" This is a car ") 

# 定义了类之后，可以用来实例化对象，并通过“对象名.成员”的方式来访问其中的数据成员或成员方法。

car = Car()
car.infor()

# 在Python中，可以使用内置方法isinstance()来测试一个对象是否为某个类的实例。
isinstance(car, Car)         # True
isinstance(car, str)         # False


# Python提供了一个关键字“pass”，表示空语句，可以用在类和函数的定义中或者选择结构中。当暂时没有确定如何实现功能，或者为以后的软件升级预留空间，或者其他类型功能时，可以使用该关键字来“占位”。
class A:
    pass

def demo():
    pass

if 5>3:
    pass
