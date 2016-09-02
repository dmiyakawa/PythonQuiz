#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''\
FizzBuzz

以下の要求を満たす関数fizzbuzz(n)を完成させてください

1から与えられた自然数n(1〜10000)までを範囲とし、
その数字を1つの改行(\\n)とともに標準出力へ出力します。
ただし、3で割り切れる場合は数字の代わりに"Fizz"、
5で割り切れる場合は"Buzz"、両者で割り切れる場合は
"FizzBuzz"を出力します。

例えばnが10の場合の回答は次のようになるはずです
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
'''

import unittest
from quiz_12 import fizzbuzz


class TestQuiz12(unittest.TestCase):
    @staticmethod
    def _expected_fizzbuzz(n):
        ret = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                ret.append('FizzBuzz\n')
            elif i % 3 == 0:
                ret.append('Fizz\n')
            elif i % 5 == 0:
                ret.append('Buzz\n')
            else:
                ret.append('{}\n'.format(i))
        return ''.join(ret)

    def _test_fizzbuzz_inter(self, n):
        import sys
        sio = None
        try:
            import io
            sio = io.StringIO()
            sio_hash = hash(sio)
            sys.stdout = sio
            fizzbuzz(n)
        except:
            self.fail('実行時に例外が発生しました')
        finally:
            sys.stdout = sys.__stdout__
        self.assertEqual(hash(sio), sio_hash)
        self.assertEqual(sio.getvalue(),
                         self.__class__._expected_fizzbuzz(n),
                         '期待通りの出力がされていないようです')

    def test_fizzbuzz(self):
        self._test_fizzbuzz_inter(10)
        self._test_fizzbuzz_inter(100)
        self._test_fizzbuzz_inter(1000)
        self._test_fizzbuzz_inter(5000)
        self._test_fizzbuzz_inter(10000)
