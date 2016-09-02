def fizzbuzz(n):
    # 1行がこれだけ長くなってしまうなら、
    # 正直なところ愚直にif, elifの羅列で良いと思います
    print('\n'.join([((((i % 3 == 0) and 'Fizz' or '')
                       + ((i % 5 == 0) and 'Buzz' or ''))
                      or str(i)) for i in range(1, n+1)]))
    # 参考:
    # http://qiita.com/kyo-bad/items/23a05c182268d3462b87
    # 上記URLのコメントには次のような解法も挙げられています
    # (ここまでくるとコードゴルフの匂いを感じる :)
    # print('\n'.join(n%3//2*'Fizz'+n%5//4*'Buzz'or str(n+1)for n in range(n)))
