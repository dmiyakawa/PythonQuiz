#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''\
時計の短針と長針間の角度

特定の時刻、時計の短針と長針間の角度を計算する
calc_degree(h, m) を完成させてください。

ここでいう時計とは12時間を1周とする
一般的なアナログ時計を指します。
hは0〜11の整数、mは0〜59の整数を取ります

戻り値は0から180度の範囲で求め、
その結果から小数点以下を切り捨てた整数とします。

例:
3時ちょうどならば引数はh=3, m=0で、正解は90です。
1時51分ならば引数はh=1, m=51で、正解は109です。
'''

import unittest
from quiz_11 import calc_degree


class TestQuiz11(unittest.TestCase):
    def test_calc_degree_1(self):
        self.assertEqual(calc_degree(0, 0), 0)
        self.assertEqual(calc_degree(1, 0), 30)
        self.assertEqual(calc_degree(2, 0), 60)
        self.assertEqual(calc_degree(3, 0), 90)
        self.assertEqual(calc_degree(4, 0), 120)
        self.assertEqual(calc_degree(5, 0), 150)
        self.assertEqual(calc_degree(6, 0), 180)

    def test_calc_degree_2(self):
        self.assertEqual(calc_degree(7, 0), 150)
        self.assertEqual(calc_degree(8, 0), 120)
        self.assertEqual(calc_degree(9, 0), 90)
        self.assertEqual(calc_degree(10, 0), 60)
        self.assertEqual(calc_degree(11, 0), 30)

    def test_cal_degree_3(self):
        self.assertEqual(calc_degree(1, 30), 135)
        self.assertEqual(calc_degree(1, 51), 109)
        self.assertEqual(calc_degree(1, 59), 65)
        self.assertEqual(calc_degree(2, 11), 0)
        self.assertEqual(calc_degree(3, 16), 2)
        self.assertEqual(calc_degree(11, 17), 123)

    def test_cal_degree_4(self):
        for h in range(0, 12):
            for m in range(0, 60):
                raw = abs(30 * h - 5.5 * m)
                if raw >= 180:
                    raw = 360 - raw
                expected = int(raw)
                self.assertEqual(calc_degree(h, m), expected)
