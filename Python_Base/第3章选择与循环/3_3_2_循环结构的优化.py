# 为了优化程序以获得更高的效率和运行速度，在编写循环语句时，应尽量减少循环内部不必要的计算，将与循环变量无关的代码尽可能地提取到循环之外。对于使用多重循环嵌套的情况，应尽量减少内层循环中不必要的计算，尽可能地向外提。

# 优化前的代码：
digits = (1, 2, 3, 4)
for i in range(1000):
    result = []
    for i in digits:
        for j in digits:
            for k in digits:
                result.append(i*100+j*10+k)

# 优化后的代码：
for i in range(1000):
    result = []
    for i in digits:
        i = i*100
        for j in digits:
            j = j*10
            for k in digits:
                result.append(i+j+k)


