#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0:
        return s
    else:
        s = s[:n] + s[n+1:]
    return s
