#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''\
クイズ4: ソート

以下の条件を満たす関数my_sort(data)を完成させてください

* 仮引数dataには全て要素が整数のリストが与えられます
* このリストの要素を大きい順に並び替えた新しいリストを返してください。
* 与えられた元のリストを破壊(変更)しないでください
'''

import unittest
from quiz_4 import my_sort


class TestQuiz4(unittest.TestCase):
    def test_my_sort_1(self):
        self.assertEqual(my_sort([2, 1, 4, 3]), [4, 3, 2, 1])
        self.assertEqual(my_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]),
                         [9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(my_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]),
                         [9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(my_sort([5, 3, 4, 2, 8, 5]),
                         [8, 5, 5, 4, 3, 2])

    def test_my_sort_2(self):
        # リストを破壊しないことをテストする
        lst = [5, 3, 4, 2, 8, 5]
        self.assertEqual(my_sort(lst), [8, 5, 5, 4, 3, 2])
        self.assertEqual(lst, [5, 3, 4, 2, 8, 5])
