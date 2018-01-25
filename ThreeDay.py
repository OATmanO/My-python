# *_ coding:UTF-8 _*_

# 位置参数


def power(x):
    return x*x


print(power(5))
print(power(255))


def power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s


print(power(5, 1))


def power(x, n):
    re = x**n
    return re


print(power(5, -1))


def add_end(L=None):
    if L is None:
        L = []

    L.append('End')
    return L
print(add_end())
print(add_end())

# 可变参数
def cal(*num):
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
print(cal(1, 2, 3, 4, 4))
print(cal(*nums))