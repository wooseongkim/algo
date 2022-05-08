# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:40:28 2020

@author: Gachon
"""

def A(a):
    x = a
    def B(b):
        return a+b
    return B

f = A(10)
print(f(20))
    