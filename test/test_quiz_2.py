#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''\
クイズ2: my_upper(s)を完成させてください

my_upper(s) はつぎのような動作をする関数とします。

 * sが文字列型ではない時、Noneを返す。
 * sが文字列型である時、文字を全て大文字にして返す。
'''

import unittest
from quiz_2 import my_upper


class CustomClass:
    def upper(self):
        return "Failed"


class TestQuiz2(unittest.TestCase):
    def test_my_upper_1(self):
        self.assertEqual(my_upper('test'), 'TEST')
        self.assertEqual(my_upper('HELLO World'), 'HELLO WORLD')
        self.assertEqual(my_upper(''), '')

    def test_my_upper_2(self):
        self.assertEqual(my_upper(b'hello binary'), None)
        obj = CustomClass()
        self.assertEqual(my_upper(obj), None)

    def test_my_upper_3(self):
        self.assertEqual(my_upper(0), None)
        self.assertEqual(my_upper({}), None)
        self.assertEqual(my_upper(()), None)
