# -*- coding: utf-8 -*-
import types

from oop.student import Student
from oop.cat import Cat
from oop.dog import Dog
from oop.animal import Animal

#
from oop.teacher import Teacher, Fib

s = Student('kk', 100)
s.hello()
print(s)

#
s.print_score()

print(s.get_name())
print(s.get_score())

d = Dog()
d.run()

c = Cat()
c.run()

# 判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(d, list))
print(isinstance(d, Animal))

# 获取对象信息 基本类型都可以用type()判断：
print(type(d) == Dog)
print(type(1) == int)
print(type([1, 2, 3]) == list)
print(type({'a': 1}) == dict)
print(type((1, 2, 3)) == tuple)
print(type({1, 2, 3}) == set)


# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(lambda x: x) == types.LambdaType)

# 实例属性和类属性
# 给实例绑定属性的方法是通过实例变量，或者通过self变量,可以看Student类


# 使用__slots__
'''
如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
'''

# 把一个getter方法变成属性，只需要加上@property就可以了
s = Student('kk', 100)
s.score = 50
print(s.score)

#定制类 比如说现在定制一个Teacher类,这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

t = Teacher(name='black')
print(t)

#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，
# Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。,参考Fib类

for i in Fib():
    print(i)

'''
Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
'''

'''
正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
class Student(object):

    def __init__(self):
        self.name = 'Michael'
调用name属性，没问题，但是，调用不存在的score属性，就有问题了：
要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
def __getattr__(self, attr):
        if attr=='score':
            return 99
'''

'''
一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
        
调用方式如下：

>>> s = Student('Michael')
>>> s() # self参数不要传入
My name is Michael.
'''