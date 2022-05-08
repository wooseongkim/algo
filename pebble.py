# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:28:15 2020

@author: Gachon
"""
import numpy as np

w = [[6, -8, 11],[7, 10, 12], [12, 14, 7], \
              [-5, 9, 4], [5, 7, 8], [3, 13, -2], \
              [11, 8, 9], [3, 5, 4]]

def getAvailPat(p):
    if p == 1:
        return 2, 3
    elif p == 2:
        return 1, 3, 4
    elif p == 3:
        return 1, 2
    else:
        return (2,)

def getPatVal(i, p):
    global w
    if p == 1:
        return w[i][0]
    elif p == 2:
        return w[i][1]
    elif p == 3:
        return w[i][2]
    else:
        return w[i][0]+w[i][2]
    
def pebble (i, p):
    if i == 0:
        return getPatVal(0, p)
    else:
        maxVal = 0
        pats = getAvailPat(p)
        for q in range(1, 5):
            if q in pats:
                tmp = pebble(i-1, q)
                if tmp > maxVal:
                    maxVal = tmp
    #print('i ', i, ' max ', maxVal)
    return maxVal+getPatVal(i, p)


def dp_pebble (n):
    peb = np.zeros((n+1, 4))
    for p in range(1, 5):
        peb[0][p-1] = getPatVal(0, p)
    for i in range(1, n+1):      
        for p in getAvailPat(np.argmax(peb[i-1])+1):        
            peb[i][p-1] = max(peb[i-1]) + getPatVal(i, p)
    return max(peb[n-1]), peb
        
maxVal, peb = dp_pebble(7)
print(maxVal)
print(peb)
#for i in range(1, 5):
#    maxVal = pebble(7, i)
#    print(maxVal)