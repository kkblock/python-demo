# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from collections import namedtuple, Counter
from collections import deque
from collections import defaultdict
from collections import OrderedDict
import struct
import hashlib
import hmac
import itertools
from contextlib import contextmanager, closing

#datetime
from urllib.request import urlopen

'''
datetime是Python处理日期和时间的标准库。
'''

now = datetime.now()
print(now)

dt = datetime(2015, 4, 19, 12, 2)
print(dt)

#把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：是一个浮点数
print(dt.timestamp())

#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

#如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
print(now.strftime('%a, %b %d %H:%M'))

#datetime加减,对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

#collections
'''
collections是Python内建的一个集合模块，提供了许多有用的集合类。
用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
'''
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

#类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1,1,1)
print(c.r)

#deque,deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict：
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

#Counter是一个简单的计数器，例如，统计字符出现的个数：
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)

#base64,Base64是一种用64个字符来表示任意二进制数据的方法。,Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。


#struct,Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
print(struct.pack('>I', 10240099))

#hashlib,Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#数据量过大,可以分次调用
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#sha1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

#hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())


#itertools
'''
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
'''
#下列代码会从1产生无限的迭代器,这里选定一个跳出条件
natuals = itertools.count(1)
for i in natuals:
    if i == 10:
        break
    print(i)

#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数,这里选择重复三次
ns = itertools.repeat('A', 3)
for i in ns:
    print(i)

#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

#groupby()
'''
groupby()把迭代器中相邻的重复元素挑出来放在一起：
实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。
如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
'''
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key,list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

#contextlib
'''
并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法：
'''
with open('/home/black/Documents/vim-help.txt', 'r') as f:
    print(f.read())

class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()

#@contextmanager
'''
编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：
其实就是返回一个对象,然后调用对象的方法
'''
class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
with create_query('Bob') as q:
    q.query()

'''
很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：
'''
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
#因此，@contextmanager让我们通过编写generator来简化上下文管理。

#@closing
'''
如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
'''
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

