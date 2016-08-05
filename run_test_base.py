#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_base.py を自前のライブラリとして呼び出す例
#

# 同一ディレクトリの test_base.py を呼びだしてくれる
import test_base

print("Before nothing")
test_base.nothing()
print("After nothing")
