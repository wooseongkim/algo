# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:54:22 2020

@author: Gachon
"""
def partition(A, p, r):
    L=[]; R=[];    
    while p < r:
        if A[p] > A[r]:
            R.append(A[p])
        else:
            L.append(A[p])
        p+= 1
    return L, R, [A[r]]

def quickSort(A, p, r):
    if p == r:
        return [A[p]]    
    L, R, q = partition(A, p, r)
    if L and R:    
        return quickSort(L, 0, len(L)-1) + q + quickSort(R, 0, len(R)-1)
    elif L:
        return quickSort(L, 0, len(L)-1) + q
    else:
        return q + quickSort(R, 0, len(R)-1)


A = [16, 5, 19, 34, 15, 9, 23, 13]
res = quickSort(A, 0, len(A)-1)
print(res)