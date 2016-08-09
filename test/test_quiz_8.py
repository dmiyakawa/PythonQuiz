#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''\
単位の変換 (1)

バイト数を表す自然数raw_sizeを受け取り、
GB(ギガバイト)単位の自然数で返す
to_gib(raw_size) を完成させてください。
余りは切り捨てます。

なお、ここで言うギガは1024の3乗です。
SI単位系のギガ(10の9乗)ではありません。
関数名ではそれを明示する意図で、
GiB(ギビバイト)を意識させるto_gib()になっています。

たとえば raw_size==24097386496ならば
正解は(24ではなく)22になります。
'''

import unittest
from quiz_8 import to_gib


class TestQuiz8(unittest.TestCase):
    def test_to_gib1(self):
        self.assertEqual(to_gib(24097386496), 22)

    def test_to_gib2(self):
        self.assertEqual(to_gib(110488033689), 102)
        self.assertEqual(to_gib(1073741823), 0)
