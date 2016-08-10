def calc_degree(h, m):
    # 一般化すると 30h - 5.5m
    # ただし解答として認められる戻り値は切り捨て後の0〜180度なので、
    # 計算後に切り捨てて0〜180以下になるように調整が必要
    degree_short = m * 6
    degree_long = (h * 30 + (30 * (m / 60)))
    diff = abs(degree_long - degree_short)
    return int(diff if diff <= 180 else 360 - diff)
