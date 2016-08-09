#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''\
クイズ7: 浮動小数点以下の切り捨て

浮動小数点数valを受け取り、
小数点以下を切り捨てた整数を返す
関数 kirisute() を実装してください。

ヒント: mathライブラリを使う問題です。
'''

import unittest
from quiz_7 import kirisute


class TestQuiz7(unittest.TestCase):
    def test_kirisute_1(self):
        self.assertEqual(kirisute(83.2), 83)
        self.assertEqual(kirisute(3.14), 3)

    def test_kirisute_2(self):
        self.assertEqual(kirisute(-123.3), -123)
        self.assertEqual(kirisute(0.0), 0)
