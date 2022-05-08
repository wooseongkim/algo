# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:02:12 2020

@author: Gachon
"""


#factoril 5! = 5* (4*3*2*1) = 120
# factor 5! = 5* 4!

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)
    

print(fib(10))