# -*- coding: utf-8 _8-

'''\
クイズ1: print("Hello World")

標準出力へ"Hello World"を出力するよう print_hello_world() を変更してください。
修正するソースコードは src/quiz_1.py にあります。
'''

import unittest
from quiz_1 import print_hello_world


class TestQuiz1(unittest.TestCase):
    def test_print_hello_world(self):
        import sys
        sio = None
        try:
            import io
            sio = io.StringIO()
            sio_hash = hash(sio)
            sys.stdout = sio
            print_hello_world()
        except:
            self.fail()
        finally:
            sys.stdout = sys.__stdout__
        self.assertEqual(hash(sio), sio_hash)
        self.assertEqual(sio.getvalue(),
                         "Hello World\n",
                         "期待通りの出力がされていないようです")
