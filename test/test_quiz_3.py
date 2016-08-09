#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''\
連長圧縮

一種の連長圧縮(Run Length Encoding)を実現する
関数encode(s)を完成させてください。

連長圧縮とは簡単な圧縮アルゴリズムの一つです。
例えば圧縮前の文字列が"aaaaabbccc"ならば、
圧縮後の文字列は"a5b2c3"となります。
文字列長は10から6となり、確かに圧縮されています。

圧縮前の文字列が"abcdefg"の場合、
圧縮後の文字列は"a1b1c1d1e1f1g1"となり、
実際には「圧縮」はされません。長くなってますので。

関数encode(s)が上記の連長圧縮の結果を返すようにしてください。
仮引数sは半角(ASCII)アルファベットだけからなる文字列です。
'''

import unittest
from quiz_3 import encode


class TestQuiz3(unittest.TestCase):
    def test_encode_1(self):
        self.assertEqual(encode("aaaaabbccc"), "a5b2c3")

    def test_encode_2(self):
        self.assertEqual(encode("abc"), "a1b1c1")

    def test_encode_3(self):
        self.assertEqual(encode("alllzzc"), "a1l3z2c1")

    def test_encode_4(self):
        self.assertEqual(encode("ttttttttttttppppqqqqqqqqqptt"),
                         "t12p4q9p1t2")

    def test_encode_5(self):
        self.assertEqual(encode(''), '')

    def test_encode_6(self):
        self.assertEqual(encode('a'), 'a1')

    def test_encode_7(self):
        self.assertEqual(encode("aaAcccBBBBBbbB"),
                         "a2A1c3B5b2B1")
