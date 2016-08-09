#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
理解度確認クイズ実行スクリプト

プロジェクト内にあるクイズについて、
回答が正しいかをテストする。

回答を src/ 下の quiz_N.py (Nは数字) に記述し、
このスクリプトでその回答に対してテストスクリプトを実行する。

クイズ0番は回答を編集することなくテストが成功するので、
まず実行してみると良い。下に実行例を示す。

    $ python --version
    Python 3.5.2
    $ python try_quiz.py 0
    test_nothing (test.test_quiz_0.TestQuiz0) ... ok

    ---------------------------------------------------
    Ran 1 test in 0.000s

    OK

クイズ1番以降は対応する src/quiz_N.py 内の関数を適切に
修正しないと「OK」と表示されない。

クイズ一覧は "python try_quiz.py -s -a" で見ることが出来る。
'''

from argparse import ArgumentParser, RawDescriptionHelpFormatter
import glob
import importlib
import os.path
import re
import sys

import unittest
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO


def print_quiz_description(quiz_index, quiz_description):
    print("----- クイズ {} -----".format(quiz_index))
    print(quiz_description)
    print()


def main():
    parser = ArgumentParser(description=(__doc__),
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('questions', metavar='question', nargs='*',
                        help='テスト実行したいクイズ番号を指定する (0, 1, ..)')
    parser.add_argument('--run-all', '-a',
                        action='store_true',
                        help='全てのクイズをテスト実行する')
    parser.add_argument('--show-description', '-s',
                        action='store_true',
                        help=('テスト実行する代わりに指定したクイズの説明を読む'))
    parser.add_argument('--use-answer', '-u',
                        action='store_true',
                        help='解答モジュールを使ってテスト実行する')
    parser.add_argument('--debug', '-d',
                        action='store_true',
                        help=('ログレベルをDEBUGへ設定する'))

    base_dir = os.path.dirname(__file__)
    args = parser.parse_args()

    logger = getLogger(__name__)
    handler = StreamHandler()
    if args.debug:
        logger.setLevel(DEBUG)
        handler.setLevel(DEBUG)
    else:
        logger.setLevel(INFO)
        handler.setLevel(INFO)
    logger.addHandler(handler)
    handler.setFormatter(Formatter('%(asctime)s %(message)s'))
    logger.debug('Start Running')

    # クイズ番号が指定されているか、--run-allが指定されていない場合、
    # これ以上実行しても意味は無い
    if not (args.questions or args.run_all):
        parser.print_help()
        return

    # 名前空間パッケージの仕組みを用いて読み込むquiz_Nモジュールを切り替える
    # Python 3.3 以降でないと動作しないはず
    if args.use_answer:
        src_dir = os.path.abspath(os.path.join(base_dir, 'src/answer'))
    else:
        src_dir = os.path.abspath(os.path.join(base_dir, 'src'))
    logger.debug("Appending src_dir \"{}\"".format(src_dir))
    sys.path.append(src_dir)

    # クイズが増えた際に手動でどこかの定数を追加でいじくる、というのは避けたい
    # 以下では可能な限り test_quiz_N.py, quiz_N.py を追加するだけで動作するようにする

    if args.show_description:
        # クイズの説明は全て test_quiz_N.py のモジュールドキュメンテーション文にある。
        # (module.__doc__で参照できる)
        if args.run_all:
            # 全ファイルを取ってきてモジュールのフォーマットに直してインポートし、
            # 各ドキュメンテーションコメントを取得する
            # ソート順はtest/test_NNN.pyの整数NNNの順
            mod_names = list(map(lambda x: x[:-3].replace('/', '.'),
                                 glob.glob('test/test*.py')))
            logger.debug("mod_names: {}".format(mod_names))
            for (quiz_index, mod_name) in \
                sorted(map(lambda name: (int(re.match(r'.+?(\d+)$', name).group(1)),
                                         name), mod_names)):
                mod = importlib.import_module(mod_name)
                print_quiz_description(quiz_index, mod.__doc__)
        else:
            # クイズ番号に従ってモジュールをインポート
            for qn in args.questions:
                quiz_index = qn
                mod = importlib.import_module('test.test_quiz_{}'.format(qn))
                print_quiz_description(quiz_index, mod.__doc__)
        return

    loader = unittest.defaultTestLoader
    if args.run_all:
        suite = loader.discover(os.path.abspath('./test'))
    else:
        tests = map(lambda x: (importlib.import_module("test.test_quiz_{}"
                                                       .format(x)),
                               "TestQuiz{}".format(x)),
                    args.questions)
        suite = unittest.TestSuite()
        for module, name in tests:
            logger.debug("module: {}, name: {}"
                         .format(module, name))
            suite.addTest(loader.loadTestsFromName(name, module=module))

    unittest.TextTestRunner(verbosity=2).run(suite)
    logger.debug('Finished Running')


if __name__ == '__main__':
    main()
