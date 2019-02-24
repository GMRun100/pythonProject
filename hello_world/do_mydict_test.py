#！/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------学习python 中单元测试的方法-----------------------
#单元测试：是指对一个函数，一个类，一个模块进行测试
#在实际的编程过程中，自己很少会进行单元测试
#假设我们编写了一个Dict类，位于文件mydict.py文件内
import unittest
from mydict import Dict

class TestDict(unittest.TestCase):  #编写测试类，从unittest.Testcase继承

    def test_init(self):             #以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d=Dict()
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

if __name__ == '__main__':
    unittest.main()