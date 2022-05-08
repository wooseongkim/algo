# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:58:16 2020

@author: Gachon
"""

a = ['a','c','e','b','b','c','e','e','a'\
     'a','b','c','e','e','d','b']
p = ['e','e','a','a','b']

def calVal(p):
    n = len(p)
    s = 0
    for i in p:
        s += pow(n-1, ord(i)-97)
        n -= 1
    return s

print(calVal(p))
a_0 = calVal(a[:len(p)])

for j in range(len(p), len(a)):
    a_0 = calVal(a[j-len(p):j])
    print(a_0)
    
        