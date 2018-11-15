# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from collections import namedtuple, Counter
from collections import deque
from collections import defaultdict
from collections import OrderedDict

#datetime
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