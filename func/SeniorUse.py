# -*- coding: utf-8 -*-
from collections import Iterable

#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L)
print(L[0:3])

#甚至什么都不写，只写[:]就可以原样复制一个list：
print(L[:])


#迭代

#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
li = [1,2,3,4,5]
for i in li:
    print(i)

#那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)


#列表生成式

#举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
print(list(range(1,11)))

print([x * x for x in range(1, 11)])