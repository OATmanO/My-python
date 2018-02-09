#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""高阶函数，返回函数，匿名函数的使用"""


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
        '''当调用_not_divisible(n)时返回的是一个新的函数，整个函数
        就是相当于filter(x%3,it),筛选去可以被3整除的'''


#
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# 判断1-1000中的回文
def is_palindrome(x):
    return str(x) == str(x)[::-1]


def yes_palindro(L1):
    return list(filter(is_palindrome, L1))


# print(yes_palindro(range(1, 1000)))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)


def by_sort(t):
    return t[1]


# print(L2)


def cont():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = cont()
print(f1())


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())


# i=0
def createcounter():
    i = 0

    def counter():
        nonlocal i
        i += 1
        return i

    return counter


countera = createcounter()
print(countera(), countera(), countera(), countera(), countera())


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
L1 = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L1)
print(L)
