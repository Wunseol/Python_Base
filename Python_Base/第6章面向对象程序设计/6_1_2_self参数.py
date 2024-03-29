# 类的所有实例方法都必须至少有一个名为self的参数，并且必须是方法的第一个形参（如果有多个形参的话），self参数代表将来要创建的对象本身。
# 在类的实例方法中访问实例属性时需要以self为前缀。
# 在外部通过对象调用对象方法时并不需要传递这个参数，如果在外部通过类调用对象方法则需要显式为self参数传值。

# 在Python中，在类中定义实例方法时将第一个参数定义为“self”只是一个习惯，而实际上不必须使用“self”这个名字，尽管如此，建议编写代码时仍以self作为方法的第一个参数名字。
class A:
    def __init__(self, v):
        self.value = v
    def show(self):
        print(self.value)
a = A(3)
a.show()
# 3








