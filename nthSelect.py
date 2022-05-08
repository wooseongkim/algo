# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:47:13 2020

@author: Gachon
"""
def partition(A):
    L=[]; R=[];
    for n in range(len(A)-1):
        if A[n] > A[-1]:
            R.append(A[n])
        else:
            L.append(A[n])
    q = len(L)
    return L, R, q, A[-1]
            
def nthSelect(A, i):
    if len(A) == 1:
        return A
    L, R, q, pivot = partition(A)
    if i < q+1:
        return nthSelect(L, i)
    elif i == q+1:
        return pivot
    else:
        return nthSelect(R, i-q-1)

A = [16, 5, 19, 34, 15, 9, 23, 13]
print(list(enumerate(sorted(A))))
res = nthSelect(A, 6)
print(6, res)