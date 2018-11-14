# -*- coding: utf-8 -*-

# try
import logging

try:
    pass
except ZeroDivisionError as e:
    pass
finally:
    pass

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError，用另一个except捕获ZeroDivisionError。
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

'''
Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
https://docs.python.org/3/library/exceptions.html#exceAndTest-hierarchy
'''
def foo():
    raise ValueError('手动抛出异常')

try:
    foo()
except ValueError as e:
    logging.exception(e)
except UnicodeError as e:
    logging.exception(e)

# 调用栈
# 记录错误 Python内置的logging模块可以非常容易地记录错误信息,同样是出错，但程序打印完错误信息后会继续执行，并正常退出：通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
logging.exception('異常信息')

#抛出错误 用raise

#断言
#凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

print(foo('1'))
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

#第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：
#python -m pdb err.py

