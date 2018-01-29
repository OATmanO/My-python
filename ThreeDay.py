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


# 关键字参数
def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)


person('mike', 20)
person('mike', 20, city='weinan')


# 命名关键字参数，若函数定义已经有了一个可变参数，后面跟着的命名关键字参数就不需要一个特殊分隔符*了
def person(name, age, *, city, job):
    print(name, age, city, job)


person('mike', 23, city='weinan', job='Student')


def person(name, age, *args, city):
    print(name, age, args, city)


# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数.
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b', b, 'c=', c, 'args=', args, kw)


def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, d, kw)


args = (1, 2, 3, 4)
atgs = (1, 2, 4)
kw = {'d': 12, 'x': '#'}
f1(*args, **kw)
f2(*atgs, **kw)


# 练习
def product(*x):
    if len(x) is 0:
        return 'Type Error'
    n = len(x)
    rest = 1
    while n > 0:
        rest = x[n-1]*rest
        n = n-1

    # for i in x:
    #    rest = rest*i

    return rest


print(product())
print(product(5))
print(product(5, 6, 7, 9))


# 别人写的好
def produce(x, *nums):
    result = x
    for num in nums:
        result *= num
    return result


print(produce(5, 6))
# 有借鉴
