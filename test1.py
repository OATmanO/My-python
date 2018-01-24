# _*_ coding : utf-8 _*_
print('the quick brown fox', 'jumps over', 'the lazy dog')

# python 中的算术
print(300 + 200)

# 分数提高了多少
s1 = 72
s2 = 85
r = s1 / s2
r = r * 100
print('小明提高了 {0:06.2f}'.format(r))
name = 123
print('{0:j^10} is a 11 length. '.format(name))

# 列表与元组的关系
classmates = list(['ma', 'te', 'emef'])
classmates.append('etets')
print(classmates[1])
classmates.insert(1, 'jaca')
print(classmates[1])
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[2][2])
# 总结列表可以修改，元组不可以修改；

# python中的条件判断
age = 3
if age >= 18:
    print('you age is %d' % age)
    print('adult')
else:
    print('you age is {0}'.format(age))
    print('teenager')
age = 1
if age >= 18:
    print('adult')
elif age > 1:
    print('teenager')
else:
    print('baby')


# 练习，小明体重问题
def weight_route(tall, weights):
    global resoult
    resoult = weights / (tall ** 2)
    if resoult <= 18.5:
        return '过轻'
    elif resoult <= 25:
        return '正常'
    elif resoult <= 28:
        return '过重'
    elif resoult <= 32:
        return '肥胖'
    elif resoult > 32:
        return '严重肥胖'
    else:
        return 'please input a ret num !'


w = 1.75
b = 80.5
f = weight_route(w, b)
print('bmi:%05.2f' % resoult)
print(f)

# python基础循环
name = ['test', 'tes2', 'test3']
for names in name:
    print(names)
sum1 = 0
for hand in range(101):
    sum1 = sum1+hand
print(sum1)
sum1 = 0
n = 1
while n < 100:
    sum1 = sum1+n
    n = n+2
print(sum1)

# 循环练习
L = ['Bart', 'Lise', 'Adam']
for i in range(3):
    print('Hello,%s!' % L[i])
n = 0
while n < 3:
    print('Hello,{0}!'.format(L[n]))
    n += 1
L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print('Hello,%s!' % i)

# list,dic,tuple,set关系
# dic，set中不能包含可变对象，tuple不可变对象，所以可以包含；
s = set(([1, 2, 3]))
m = {(1, 2, 3)}
print(s)

# 函数
import math

x = [12.3, 14.2, 14.5]


def area_of_circle(arg):
    output = arg*arg*math.pi
    return output


for i in x:
    s = area_of_circle(i)
    print(s)
    print(round(s, 3))
