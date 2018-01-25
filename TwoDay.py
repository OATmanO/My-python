# _*_ coding : utf-8 _*_

# 绝对值函数
print(abs(-100))
print(abs(12.3))


# 比较函数
x = [1, 2, 3, 4, 5]
print(max(1, 2))
print(max(x))


# 数据类型转换
print(int('123'))
print(int(12.3))
float('12.34')
print(str('123'))
print(bool(1))
a = abs #函数名
print(a(-12))

n1 = 255
n2 = 1000
print('所得的十六进制数为：%s' % hex(255))


# 定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-9))


def may_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 函数返回多个值 tuple
import math


def move(x, y, step, angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx, ny


x, y = move(100, 200, 20, math.pi/6)
print(x, y)
r = x, y
print(r)

# 首先应对参数的数据类型做检查


def quadratic(a, b, c):
    if b**2-4*a*c == 0:
        x1 = -b/2/a
        x2 = x1
        return x1, x2
    elif (b**2-4*a*c) >= 0:
        x1 = (-b+math.sqrt(b**2-4*a*c))/2/a
        x2 = (-b-math.sqrt(b**2-4*a*c))/2/a
        return x1, x2
    elif (b**2-4*a*c) <= 0:
        return "该函数没有解"
    else:
        return "该函数没有解"


t = [1, 2, 3]
print(quadratic(t[0], t[1], t[2]))
print('二元一次方程%sx*2+%sx+%s=0的解为:' % (t[0], t[1], t[2]), quadratic(t[0], t[1], t[2]))

# ThreeDay tips
print(quadratic(*t))
print('二元一次方程%sx*2+%sx+%s=0的解为:' % (t[0], t[1], t[2]), quadratic(*t))
print('二元一次方程{0}x*2+{1}x+{2}=0的解为:'.format(*t), quadratic(*t))

