# これは何か

Python 練習用クイズ集です。

開発時には Python3.5.2 で動作検証しました。
Python 3.3以降でないと動作しないはずです。

事前にバージョンが適切であることを確認してください。

    $ python --version
    Python 3.5.2


## 概要

このクイズ集は複数のクイズから構成され、
それぞれのクイズには1から始まる整数が割り振られています。

それぞれのクイズに対して関連するファイルが次のように存在します

* src/quiz_N.py ... (未完成の)ソースコード
* test/test_quiz_N.py ... ソースコードをテストするスクリプト
* src/answer/quiz_N.py ... 回答例のソースコード

学習者は src/quiz_N.py の中にある所定の関数を修正し、テストが成功するようにしてください。

テストを実行するにはプロジェクトのトップディレクトリにある
テスト実行スクリプト ```try_quiz.py``` を実行します。

テスト0番は例外的に、なにもしないで成功するようになっています。
以下に実行例を示します。

    $ python try_quiz.py 0
    test_nothing (test.test_quiz_0.TestQuiz0) ... ok

    ---------------------------------------------------
    Ran 1 test in 0.000s

    OK

テスト1番以降はそうはなっていません


    $ python try_quiz.py 1
    test_print_hello_world (test.test_quiz_1.TestQuiz1) ... FAIL
    
    ======================================================================
    FAIL: test_print_hello_world (test.test_quiz_1.TestQuiz1)
    ----------------------------------------------------------------------
    ...
    (省略)
    ...
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
    
    FAILED (failures=1)

ここで仮に ```src/quiz_1.py``` を正しく修正しておくと、
このテストでも次のようにOKと表示されるようになります。

    $ python try_quiz.py 1
    test_print_hello_world (test.test_quiz_1.TestQuiz1) ... ok
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s
    
    OK

この「テストをOKにしていく作業」が本プロジェクトでの学習者の目的です。

全てのクイズを試すには```python try_quiz.py -a```とします。
このテストでOKが出れば、練習は完了です。


## 回答例について

各クイズには回答例が付属しています。
クイズN番に対する回答例は```src/answer/quiz_N.py```にあります。

回答例はプロジェクトをダウンロードした時点で付属の全テストに
成功するようにできています。
言い換えると、本プロジェクト自体をテストするのに使います。

## 問題と回答の正確さについて (言い訳)

本問題集は入門者向けに簡便な練習を提供する目的で作られているため、
いわゆるプログラミングコンテストのように厳しく回答をチェックしていません。

あくまでPython入門として、いくつかの関数やステートメントを使用するだけで
回答できる程度のクイズと、それを大雑把に確認するテストスクリプトが入っています。
あまり厳しいコーナーケース
（例えば「整数のリストとしか書いてないのだから、サイズが1兆個のリストでも動作するべきだ」といった）
については考慮・検証してませんのでご了承ください。
クイズのそれぞれに 1<= L <= 1,000,000 などと境界条件を書けば、
問題の記述はより厳密になりますが、逆にとっつきづらくなる懸念があるため、
このプロジェクトでは採用しません。

O-記法まわりの理解が必要な問題も基本的に存在しません。
アルゴリズムに関する勉強は他の豊富なリソースがありますので、
このプロジェクトで達成する目標からは外しています。

ただ、もし説明や回答例の中に、特に初心者にとって自明に混乱をまねく表現等があった場合には
それはバグとみなすべきかもしれません。Issue、PRをお待ちしております。


## おまけ

同じテストを利用しつつ参照するモジュールを動的に切り替える
(演習用の```src/quiz_N.py```と```src/answer/quiz_N.py```を切り替える)
方法に一番手間取りました。

