#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def accumulate(start, end, handle, init_value, combine):

  def symbol(a, b, combine):
    if '+' == combine:
      return a + b
    elif '*' == combine:
      return a * b
    else:
      pass  # 错误处理

  total = init_value
  for x in range(start, end + 1):
    total = symbol(total, handle(x), combine)
  return total

def sum(start, end, handle):
  return accumulate(start, end, handle, 0, '+')

def product(start, end, handle):
  return accumulate(start, end, handle, 1, '*')

def identity(n):
  return n

print(sum(1, 100, identity))
print(product(1, 6, identity))


def add(start,end):
    return reduce((lambda x,y:x+y),[x for x in range(start, end+1)])

print(add(1,100))


def add1(start, end, hand):
    return reduce((lambda x, y: x+y), map(lambda x: hand(x), [x for x in range(start, end+1)]))
def indentity(n):
    return n
print(add1(1,100,indentity))

def adf(x,y,f):
    return f(x)+f(y)
print(adf(-5,-6,abs))




def normalize(name):
    rename = name[0].upper()+name[1:].lower()
    return rename


L1 = ['adma', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce((lambda x,y:x*y),L)
L3=[3,5,7,9]
print(prod(L3))


def str2folat(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
    def char2num(s):
        return DIGITS[s]
    def fladt(x,y):
        if y == '.':
            return x
        else:
            return x*10+y
    return reduce(fladt,map(char2num,s))/10**len(s.split('.')[1])

print(str2folat('134234.234123'))


