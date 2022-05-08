# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
key =[10, 20, 25, 30, 35, 40, 45]
def treeSearch(t, s, x):
    global key
    if t == 0 or key[t] == x:
        return t;
    if x < key[t]:
        return treeSearch(t-(s//2 +1), s//2, x)
    else:
        return treeSearch(t+(s//2 +1), s//2, x)

res = treeSearch(3, len(key)//2, 10)
print(key[res])