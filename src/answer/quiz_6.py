def gcd(a, b):
    if a < b:
        gcd(b, a)
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)
