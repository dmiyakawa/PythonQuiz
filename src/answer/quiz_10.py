# -*- coding: utf-8 -*-
import string


def decode(s):
    current_ch = None
    current_length = None
    ret = []
    for c in s:
        if c in string.ascii_letters:
            if current_length:
                ret.append(current_ch * current_length)
            current_ch = c
            current_length = 0
        elif c in string.digits:
            current_length = (current_length*10) + int(c)
        else:
            raise RuntimeError('Unexpected char "{}"'.format(c))
    if current_length:
        ret.append(current_ch * current_length)
    return ''.join(ret)
