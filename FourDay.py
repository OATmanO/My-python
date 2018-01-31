# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)


print(fact(2))


# 改成尾递归
def fact(n):
    return fact1(n, 1)


def fact1(nums, product):
    if nums == 1:
        return product
    return fact1(nums-1, nums*product)


print(fact(2))


# 迭代
def fact2(n):
    result = 1
    for i in range(2, n+1):
        result *= i
        return result


print(fact2(2))


# 汉诺塔问题，未解决
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


move(3, 'A', 'B', 'C')
