# -*- coding: utf-8 -*-

import unittest

'''
单元测试,为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：
编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。
最常用的断言就是assertEqual()：
另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
with self.assertRaises(KeyError):
    value = d['empty']
    
运行单元测试
if __name__ == '__main__':
    unittest.main()
直接运行python文件或者python -m unittest mydict_test

setUp与tearDown
相当于java的 before after
'''

if __name__ == '__main__':
    unittest.main()


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
