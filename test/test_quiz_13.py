#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''\
対戦表のチェック

4高校対抗の運動会を行うとします。
4人ずつ選出され、4人のうち一人を選んで、
各競技毎に勝敗を競います。

この際、競技で発生する対戦者の組み合わせは
4高校4選手から256通り(4の4乗)通りしかありません。

以上をふまえ、与えられた4選手の名前を見て、
あり得る組み合わせであるかをチェックする
check(a, b, c, d)を作成してください。
あり得る組み合わせならばTrueを、
あり得ないようならFalseを返します。

4校の選手名は編集前のソースコード中に
含まれているものを使用するものとします。
'''

import unittest
from quiz_13 import check

# school_1 = ['くにお', 'すがた', 'ななせ', 'たかみね']
# school_2 = ['りき', 'さおとめ', 'まえだ', 'よしの']
# school_3 = ['りゅういち', 'りゅうじ', 'こばやし', 'もちづき']
# school_4 = ['よりつね', 'みつさだ', 'くわたり', 'あかぼし']


class TestQuiz13(unittest.TestCase):
    def test_check_1(self):
        self.assertEqual(True, check('くにお', 'りき', 'りゅういち', 'よりつね'))
        self.assertEqual(True, check('ななせ', 'よしの', 'りゅうじ', 'あかぼし'))

    def test_check_2(self):
        self.assertEqual(True, check('さおとめ', 'みつさだ', 'こばやし', 'たかみね'))
        self.assertEqual(True, check('みつさだ', 'りゅういち', 'くにお', 'さおとめ'))
        self.assertEqual(True, check('もちづき', 'くわたり', 'くにお', 'りき'))

    def test_check_3(self):
        self.assertEqual(False, check('くにお', 'たかみね', 'りゅうじ', 'よりつね'))
        self.assertEqual(False, check('さおとめ', 'あかぼし', 'みつさだ', 'すがた'))
        self.assertEqual(False, check('くにお', 'くにお', 'くにお', 'くにお'))

    def test_check_4(self):
        self.assertEqual(False, check('くにお', 'きり', 'りゅういち', 'よりつね'))
        self.assertEqual(False, check('もちづき', 'もりもと', 'くにお', 'くわたり'))
        self.assertEqual(False, check('くにお', 'しみず', 'はやさか', 'こばやし'))
