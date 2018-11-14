# -*- coding: utf-8 -*-
import types

from oop.student import Student
from oop.cat import Cat
from oop.dog import Dog
from oop.animal import Animal
#
s = Student('kk',100)
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

#判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(d,list))
print(isinstance(d,Animal))

#获取对象信息 基本类型都可以用type()判断：
print(type(d) == Dog)
print(type(1) == int)
print(type([1,2,3]) == list)
print(type({'a':1}) == dict)
print(type((1,2,3)) == tuple)
print(type({1,2,3}) == set)

#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
def fn():
    pass

print(type(fn) ==types.FunctionType)
print(type(lambda x: x)==types.LambdaType)

#实例属性和类属性
#给实例绑定属性的方法是通过实例变量，或者通过self变量,可以看Student类