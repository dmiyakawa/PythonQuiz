#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''\
クイズ6: 最大公約数

2つの非負整数a, bを受け取り、
最大公約数を返すgcd(a, b)を実装してください。

なお、これは数学の試験ではないので
「ユークリッドの互除法」でWeb検索して
出てきたアルゴリズムを実装すれば十分です。
'''

import unittest
from quiz_6 import gcd


class TestQuiz6(unittest.TestCase):
    def test_gcd_1(self):
        self.assertEqual(gcd(5, 15), 5)
        self.assertEqual(gcd(2, 2), 2)
        self.assertEqual(gcd(9, 2), 1)

    def test_gcd_2(self):
        self.assertEqual(gcd(1029, 1071), 21)

    def test_gcd_3(self):
        self.assertEqual(gcd(258937003, 33108243), 1)
        # 流石にあまりに酷なのでコメントアウト
        # https://en.wikipedia.org/wiki/Gigantic_prime
        # import sys
        # limit = sys.getrecursionlimit()
        # sys.setrecursionlimit(limit * 100)
        # self.assertEqual(gcd((2**44497 - 1) * 13, (10**9999 + 33603) * 13),
        #                  13)
        # sys.setrecursionlimit(limit)
