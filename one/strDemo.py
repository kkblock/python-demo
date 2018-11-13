# -*- coding: utf-8 -*-

print("this is a python demo")

#格式化
print('Hello, %s' % 'world')

''' 常用占位符
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
'''
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

#转义 %
print('growth rate: %d %%' % 7)

#另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))