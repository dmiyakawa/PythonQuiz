school_1 = ['くにお', 'すがた', 'ななせ', 'たかみね']
school_2 = ['りき', 'さおとめ', 'まえだ', 'よしの']
school_3 = ['りゅういち', 'りゅうじ', 'こばやし', 'もちづき']
school_4 = ['よりつね', 'みつさだ', 'くわたり', 'あかぼし']


# a, b, c, d の組み合わせが256個しかないので
# リストによる線形探査でいーだろ、という回答
valid_combinations = [{a, b, c, d}
                      for a in school_1
                      for b in school_2
                      for c in school_3
                      for d in school_4]


def check(a, b, c, d):
    return {a, b, c, d} in valid_combinations
