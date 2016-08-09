def to_gib2(raw_size):
    return "{:,.2f}".format(round(raw_size / (1024**3), 2))
