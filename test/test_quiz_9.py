#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''\
単位の変換 (2)

バイト数を表す自然数raw_sizeを受け取り、
GB(ギガバイト)単位の文字列で返す
to_gib2(raw_size) を完成させてください。
ここで言うギガは1024の3乗です。

文字列には小数点以下2桁までを含めます。
余りは四捨五入してください。

たとえば raw_size==24097386496 ならば
正解は"22.44"になります。
'''

import unittest
from quiz_9 import to_gib2


class TestQuiz9(unittest.TestCase):
    def test_to_gib1(self):
        self.assertEqual(to_gib2(24100135239), '22.44')
        self.assertEqual(to_gib2(24100135240), '22.45')
        self.assertEqual(to_gib2(1063004406), '0.99')

    def test_to_gib2(self):
        self.assertEqual(to_gib2(110488033689), '102.90')
        self.assertEqual(to_gib2(1073741823), '1.00')
