# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:52:47 2020

@author: Gachon
"""
def matrixPath(n):
    for i in range(1,len(n)):
        for j in range(1,len(n)):
            n[i][j] = n[i][j] + max(n[i-1][j], n[i][j-1])
    print(n)

mat = [ [0, 0, 0, 0, 0],
        [0, 6, 7, 12, 5],
        [0, 5, 3, 11, 18],
        [0, 7, 17, 3, 3],
        [0, 8, 10, 14, 9]]
matrixPath(mat)