# 通过关键参数，实参顺序可以和形参顺序不一致，但不影响传递结果，避免了用户需要牢记位置参数顺序的麻烦。

def demo(a,b,c=5):
    print(a,b,c)

demo(3,7)
# 3 7 5
print(demo(a=7,b=3,c=6))
# 7 3 6
print(demo(c=8,a=9,b=0))
# 9 0 8
