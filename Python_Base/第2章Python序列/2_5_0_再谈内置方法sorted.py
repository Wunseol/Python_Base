# 列表对象提供了sort()方法支持原地排序，而内置函数sorted()返回新列表，并不对原列表进行任何修改。
# sorted()方法可以对列表、元组、字典、range对象等进行排序。
# 列表的sort()方法和内置函数sorted()都支持key参数实现复杂排序要求。


persons = [{'name':'Dong', 'age':37}, 
               {'name':'Zhang', 'age':40},
               {'name':'Li', 'age':50},
               {'name':'Dong', 'age':43}]
print(persons)
# [{'name': 'Dong', 'age': 37}, {'name': 'Zhang', 'age': 40}, {'name': 'Li', 'age': 50}, {'name': 'Dong', 'age': 43}]

phonebook = {'Linda':'7750', 'Bob':'9345', 'Carol':'5834'}
from operator import itemgetter
#itemgetter函数用于获取对象的哪些维的数据
print(sorted(phonebook.items(), key=itemgetter(1)))                                     #按字典中元素值进行排序
# [('Carol', '5834'), ('Linda', '7750'), ('Bob', '9345')]
print(sorted(phonebook.items(), key=itemgetter(0)))
                                     #按字典中元素的键进行排序
# [('Bob', '9345'), ('Carol', '5834'), ('Linda', '7750')]

gameresult = [['Bob', 95.0, 'A'], ['Alan', 86.0, 'C'], 
                  ['Mandy', 83.5, 'A'], ['Rob', 89.3, 'E']]
print(sorted(gameresult, key=itemgetter(0, 1)))
                             #按姓名升序，姓名相同按分数升序排序
# [['Alan', 86.0, 'C'], ['Bob', 95.0, 'A'], ['Mandy', 83.5, 'A'], ['Rob', 89.3, 'E']]
print(sorted(gameresult, key=itemgetter(1, 0)))
                             #按分数升序，分数相同的按姓名升序排序
# [['Mandy', 83.5, 'A'], ['Alan', 86.0, 'C'], ['Rob', 89.3, 'E'], ['Bob', 95.0, 'A']]
print(sorted(gameresult, key=itemgetter(2, 0)))
                             #按等级升序，等级相同的按姓名升序排序
# [['Bob', 95.0, 'A'], ['Mandy', 83.5, 'A'], ['Alan', 86.0, 'C'], ['Rob', 89.3, 'E']]

gameresult = [{'name':'Bob', 'wins':10, 'losses':3, 'rating':75.0},
                  {'name':'David', 'wins':3, 'losses':5, 'rating':57.0},
                  {'name':'Carol', 'wins':4, 'losses':5, 'rating':57.0},
                  {'name':'Patty', 'wins':9, 'losses':3, 'rating':72.8}]
print(sorted(gameresult, key=itemgetter('wins', 'name')))
#按'wins'升序，该值相同的按'name'升序排序
# [{'name': 'David', 'wins': 3, 'losses': 5, 'rating': 57.0}, {'name': 'Carol', 'wins': 4, 'losses': 5, 'rating': 57.0}, {'name': 'Patty', 'wins': 9, 'losses': 3, 'rating': 72.8}, {'name': 'Bob', 'wins': 10, 'losses': 3, 'rating': 75.0}]

# 根据另外一个列表的值来对当前列表元素进行排序
list1 = ["what", "I'm", "sorting", "by"]
list2 = ["something", "else", "to", "sort"]
pairs = zip(list1, list2)
pairs = sorted(pairs)
print(pairs)
# [("I'm", 'else'), ('by', 'sort'), ('sorting', 'to'), ('what', 'something')]
result = [x[1] for x in pairs]
print(result)
# ['else', 'sort', 'to', 'something']


