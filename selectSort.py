# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:16:01 2020

@author: Gachon
"""
def selectSort(subList, n):
    maxItem = 0
    if n == 1:
        return subList[0]
    else:
        for i in range(n):
            if subList[i] > subList[maxItem]:
                maxItem = i;
        #swap
        subList[n-1], subList[maxItem] = \
        subList[maxItem], subList[n-1]
        selectSort(subList, n-1)
        
a = [2, 4, 1, 5, 7];
selectSort(a, 5)
print(a)

            