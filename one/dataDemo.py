# -*- coding: utf-8 -*-

#list 列表

#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

#可以用索引来访问
print(classmates[0])
#最后一个元素的索引是len(classmates) - 1,还可以用-1做索引，直接获取最后一个元素：
print(len(classmates)-1)
print(classmates[-1])

#把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
print(classmates)

#要删除list末尾的元素，用pop()方法：
classmates.pop(1)
print(classmates)

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[0] = 'kk'
print(classmates)

#list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]
print(L)

#list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)


# tuple 元组 不能修改

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
'''
classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素
#不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
'''

#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t = (1, 2)
print(t)
#如果要定义一个空的tuple，可以写成()：
#但是，要定义一个只有1个元素的tuple,需要加一个,
t = (1,)
print(t[0])

# 若元组内包含列表,则可以改变列表的内容
t = (1,2,['A','B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
# t[2][2] = 'Z'#这不生效
print(t)


#使用dict和set
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在,二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
# print(d.get('Thomas'))
print(d.get('Thomas', 1))

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
print(d)

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#要创建一个set，需要提供一个list作为输入集合,add()增加元素 remove移除元素
s = {1, 2, 3, 1}
print(s)















