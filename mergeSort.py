# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:16:01 2020

@author: Gachon
"""
def merge(subList, p, q, r):    
    L = subList[p:q+1] 
    R = subList[q+1:r+1] 
    i = p;
    print('sublist ', subList, 'left ', L, ' right ', R)
    lp = 0;    rp = 0;
    print('pqr is ', p, q, r)
    while lp <= len(L)-1 and rp <= len(R)-1: 
        if L[lp] <= R[rp]: 
            subList[i] = L[lp]
            lp += 1 
        else: 
            subList[i] = R[rp]
            rp += 1
        i += 1
    if lp > q:
        while rp <= len(R)-1:
            subList[i] = R[rp]
            rp += 1
            i += 1
    else:
        while lp <= len(L)-1:
            subList[i] = L[lp]
            lp += 1
            i += 1

    print('merge ', subList)
    
        
def mergeSort(subList, p, r):
    if p < r:
        q = (p+r)//2 #floor
        mergeSort(subList, p, q)
        mergeSort(subList, q+1, r)
        merge(subList, p, q, r)
        
a = [2, 7, 1, 5, 4, 9];
mergeSort(a, 0, 5)
print(a) 
#merge([4, 2, 8], 0, 1, 2)
            