# -*- coding: utf-8 -*-


def encode(s):
    length = 0
    current_char = None
    # Python「っぽい」とされる書き方なのでこうしている
    # ''.join(['a', 'b', 'c']) -> 'abc'
    # 今回は単に ret = ""として ret += "a3" などと結合しても問題はない
    ret = []
    # "aaaaabbccc"なら、最初のaから順に変数cに入れられてブロック内が実行される
    for c in s:
        # current_charは1つ前のループの文字、つまり直前の文字を保持している
        # current_char == c とは「前後で同じ文字であるということ」
        # current_charは最初はNoneなので、1文字目では必ずelseブロックへ行く
        if current_char == c:
            # 連長圧縮では文字の連続した数をカウントしておくのでlengthに1足す
            length += 1
        else:
            # 1文字目、もしくは前後で異なる文字が来た際にこちらのブロックへ来る
            # もしcurrent_charに意味のある文字が入っているなら、
            # それは"aabb"で言えばaからbへの切り替わりを意味する。
            # その際には"a2"をretに突っ込んでおく必要がある。
            if current_char:
                ret.append('{}{}'.format(current_char, length))
            # current_charとlengthを現在の文字向けにリセットする
            current_char = c
            length = 1
    # 文字列の最後に来た際にcurrent_charがNoneでなければ
    # その文字についても圧縮後の文字列に含める必要がある
    # Noneの場合は圧縮前の文字列が空を意味するので、なにも足さない。
    if current_char:
        ret.append('{}{}'.format(current_char, length))

    return ''.join(ret)
