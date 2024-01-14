# 函数定义时括弧内为形参，一个函数可以没有形参，但是括弧必须要有，表示该函数不接受参数。
# 函数调用时，将实参的引用传递给形参。
# 在定义函数时，对参数个数并没有限制，如果有多个形参，需要使用逗号进行分隔。

# 对于绝大多数情况下，在函数内部直接修改形参的值不会影响实参，而是创建一个新变量。例如：
def addOne(a):
    print(id(a), ':', a)#注意：此时a的地址与v的地址相同
    a += 1
    print(id(a), ':', a)#现在a的地址和v的地址不一样了
v = 3
print(id(v))
# 1599055008
print(addOne(v))
# 1599055008 : 3
# 1599055040 : 4
print(v)
# 3
print(id(v))
# 1599055008


# 在有些情况下，可以通过特殊的方式在函数内部修改实参的值。
def modify(v):          # 使用下标修改列表元素值
    v[0] = v[0]+1

a = [2]
modify(a)
print(a)
# [3]
def modify(v, item):    # 使用列表的方法为列表增加元素
    v.append(item)

a = [2]
modify(a,3)
print(a)
# [2, 3]


# 也就是说，如果传递给函数的实参是可变序列，并且在函数内部使用下标或可变序列自身的原地操作方法增加、删除元素或修改元素时，实参也得到相应的修改。

def modify(d):         #修改字典元素值或为字典增加元素
    d['age'] = 38
a = {'name':'Dong', 'age':37, 'sex':'Male'}
print(a)
# {'age': 37, 'name': 'Dong', 'sex': 'Male'}
modify(a)
print(a)
# {'age': 38, 'name': 'Dong', 'sex': 'Male'}


