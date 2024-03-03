# 继承是用来实现代码复用和设计复用的机制，是面向对象程序设计的重要特性之一。设计一个新类时，如果可以继承一个已有的设计良好的类然后进行二次开发，无疑会大幅度减少开发工作量。
# 在继承关系中，已有的、设计好的类称为父类或基类，新设计的类称为子类或派生类。派生类可以继承父类的公有成员，但是不能继承其私有成员。如果需要在派生类中调用基类的方法，可以使用内置函数super()或者通过“基类名.方法名()”的方式来实现这一目的。
class Person(object) :
    sex='male'
    def __init__(self, s1, s2):
        self.IDcard=s1
        self.name=s2
        print('__init__(self) of Person')
    def hello(self, friend):
        print('hello, ','friend','!')

class Student(Person):  #子类Student，父类Person
    def __init__(self, num):
        self.number=num
        
    def fun(self):
         print (self.IDcard, self.name,self.number, Student.sex)


class Teacher(Person): #子类Teacher, 父类Person
    def __init__(self, t, s1, s2):
        self.title=t
        super(Teacher,self).__init__(s1, s2)          #调用父类的构造函数
    def fun(self):
        print(self.IDcard, self.name, self.title, Teacher.sex)


#主程序
stud1=Student('2012009')
stud1.IDcard='533001198006250079'
stud1.name='Wang Ming'
stud1.fun()
stud1.hello('Yang')
teach1=Teacher('professor', '533001197012130055', 'Yang Lipin')
Teacher.sex='female' 
teach1.fun()
teach1.hello('Wang')

# self的注意事项：在继承时，传入的是哪个实例，就是那个传入的实例，而不是指self的父类的实例。
# 程序：
class Parent:
    def pprt(self):
        print(self)

class Child(Parent):
    def cprt(self):
        print(self)

c = Child()
c.cprt()
c.pprt()
p = Parent()
p.pprt()              


# 解释：
# 运行c.cprt()时应该没有理解问题，指的是Child类的实例。
# 但是在运行c.pprt()时，等同于Child.pprt(c)，所以self指的依然是Child类的实例，由于self中没有定义pprt()方法，所以沿着继承树往上找，发现在父类Parent中定义了pprt()方法，所以就会成功调用。

# 注：
# self在定义时需要定义，但是在调用时会自动传入。
# self总是指调用时的类的实例。



