school_1 = ['くにお', 'すがた', 'ななせ', 'たかみね']
school_2 = ['りき', 'さおとめ', 'まえだ', 'よしの']
school_3 = ['りゅういち', 'りゅうじ', 'こばやし', 'もちづき']
school_4 = ['よりつね', 'みつさだ', 'くわたり', 'あかぼし']

#
# 各校の選手数が大きくなった場合、以下の回答は不適切な可能性が高い。
# 例えば1000人ずついたとすると、リストは1000の4乗で、
# 線形探査には全く向かない。
#

# a, b, c, d の組み合わせが256個しかないので
# リストによる線形探査でいーだろ、という回答
valid_combinations = [{a, b, c, d}
                      for a in school_1
                      for b in school_2
                      for c in school_3
                      for d in school_4]


def check(a, b, c, d):
    return {a, b, c, d} in valid_combinations
