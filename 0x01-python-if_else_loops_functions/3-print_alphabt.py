#!/usr/bin/python3
def printing_alpha():
    for alpha in range(ord('a'), ord('z') + 1):
        if chr(alpha) not in ('q', 'e'):
            print(chr(alpha), end='')
    
printing_alpha()
