#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''\
クイズ5: ソート(2)

以下の条件を満たす関数my_sort(data)を完成させてください

* 仮引数dataには全て要素が非負整数のリストが与えられます
* このリストの要素を次の条件で並び替えた新しいリストを返してください。
** 3で割った余りが大きい方が前にくること
** 3で割った余りが同じ場合、元の数が大きい方が前にくること
* 与えられた元のリストを破壊(変更)しないでください

入力が[1, 2, 3, 4]ならば、[2, 4, 1, 3] が返される結果になります。
なぜなら、

* 3で割った余りが一番大きいのは2である (余りは2)
* 3で割った余りが次に大きいのは1, 4である (余りは1)
* 4 > 1 なので、4が1の前に来る
* 3が最後に来る (余りは0)
'''

import unittest
from quiz_5 import my_sort


class TestQuiz5(unittest.TestCase):
    def test_my_sort_1(self):
        self.assertEqual(my_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                         [8, 5, 2, 7, 4, 1, 9, 6, 3, 0])
        self.assertEqual(my_sort([2, 1, 4, 3]), [2, 4, 1, 3])

    def test_my_sort_2(self):
        lst = [5, 3, 4, 2, 8, 5, 11]
        self.assertEqual(my_sort(lst), [11, 8, 5, 5, 2, 4, 3])
        self.assertEqual(lst, [5, 3, 4, 2, 8, 5, 11])
