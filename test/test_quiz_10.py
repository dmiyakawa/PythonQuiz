#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''\
連長圧縮 (2)

連長圧縮(Run Length Encoding)された文字列を
元の文字列に展開する関数decode(s)を完成させてください

連長圧縮とは簡単な圧縮アルゴリズムの一つです。
例えば圧縮前の文字列が"aaaaabbccc"ならば、
圧縮後の文字列は"a5b2c3"となります。
文字列長は10から6となり、確かに圧縮されています。

圧縮前の文字列が"abcdefg"の場合、
圧縮後の文字列は"a1b1c1d1e1f1g1"となり、
実際には「圧縮」はされません。

関数 decode(s) は連長圧縮後の文字列を受け取ります。
元の文字列はsは半角(ASCII)アルファベットだけからなる文字列です。
(クイズ「連長圧縮」も参照してください)

本問題ではアルファベットの後に続く数字は負でない整数
となる数字(0〜9)の並びであるとします。
'''

import unittest
from quiz_10 import decode


class TestQuiz10(unittest.TestCase):
    def test_decode_1(self):
        self.assertEqual(decode('a5b2c3'), 'aaaaabbccc')

    def test_decode_2(self):
        self.assertEqual(decode('a1b1c1'), 'abc')

    def test_decode_3(self):
        self.assertEqual(decode('a1l3z2c1'), 'alllzzc')

    def test_decode_4(self):
        self.assertEqual(decode('t12p4q9p1t2'),
                         'ttttttttttttppppqqqqqqqqqptt')

    def test_decode_5(self):
        self.assertEqual(decode(''), '')

    def test_decode_6(self):
        self.assertEqual(decode('a1'), 'a')

    def test_decode_7(self):
        self.assertEqual(decode('a2A1c3B5b2B1'),
                         'aaAcccBBBBBbbB')

    def test_decode_8(self):
        self.assertEqual(decode('a2215z321y92'),
                         (('a'*2215) + ('z'*321) + 'y'*92))

    def test_decode_9(self):
        self.assertEqual(decode('a0000b0c00'), '')
