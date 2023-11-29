#!/usr/bin/python3
def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        print("Error: Both inputs must be integers")
