# -*- coding: utf-8 -*-
from functools import reduce
'''
高阶函数的一些例子
'''

#map map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

def f(x):
    return x * x

r = map(f,list(range(10)))
print(list(r))

#reduce 比方说对一个序列求和，就可以用reduce实现,这个函数必须接收两个参数

def add(x,y):
    return x+y

r = reduce(add,list(range(1,10)))
print(r)

'''
当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。
但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
'''
def fn(x,y):
    return x*10 + y

print(reduce(fn,[1,3,5,7,9]))

#Python内建的filter()函数用于过滤序列。
'''
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

#把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

'''
注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
'''

#Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))
#此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))

#字符串排序 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

#这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


#匿名函数

