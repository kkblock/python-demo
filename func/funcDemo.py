# -*- coding: utf-8 -*-
import math

print(abs(100))
print(abs(-20))

print(max(2, 3, 1, -5))

print(int('123'))
print(float('12.34'))
print(bool(1))


# 定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(2))
print(my_abs(-2))


# 空函数
def nop():
    pass


'''
当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。

让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
'''


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(10))


# print(my_abs(x='a')) #这里将会抛出异常信息

# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#可变参数,可传入多个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3))

#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
print(calc(*nums))

#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#命名关键字参数,和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

