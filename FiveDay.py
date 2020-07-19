# 高级特性
# 切片
L = ['Nicdh', 'sarch', 'targ', 'bob', 'jack']
print(L[0])

r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
print(L[:3])
print(L[1:3])

L = list(range(100))

print(L[:10])
print(L[:10:2])


# 去掉字符串首尾空格
def trim(s):
    s = s[1:-1]
    return s


tring = ' abjg '
print(trim(tring))

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

import collections.abc

print(isinstance('abc', collections.abc.Iterable))
print(isinstance(123, collections.abc.Iterable))

for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)


# 使用迭代查找list中最小值和最大值，返回一个tuple
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    Max = L[0]
    Min = L[0]
    for value in L:
        if value > Max:
            Max = value
        if value < Min:
            Min = value
    return (Max, Min)


print(findMinAndMax([1, 2, 3, 4]))

print([x * x for x in range(1, 10)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'Abc' for n in 'def'])
import os

print([d for d in os.listdir('.')])
d = {'a': '1', 'b': '2', 'c': '3'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 'IBM', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s, collections.abc.Iterable) is True]
print(L2)

g = (x * x for x in range(10))
print(next(g))
for n in g:
    print(n)


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(n, b)
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib(8))


# 大佬牛皮
def triangle():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]


o = triangle()
print(next(o))
print(next(o))
print(next(o))
print(next(o))
