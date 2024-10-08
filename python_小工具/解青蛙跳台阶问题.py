


def frog(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return frog(n-1) + frog(n-2)

result = frog(20)
print(result)


