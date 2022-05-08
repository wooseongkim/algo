# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:07:02 2020

@author: Gachon
"""

def heapify(arr, n, i):
  p = i
  l = 2 * i + 1 #left child
  r = 2 * i + 2 #right child

  if l < n and arr[p] > arr[l]:
	  p = l
  if r < n and arr[p] > arr[r]:
	  p = r

  if p != i:
	  arr[i], arr[p] = arr[p], arr[i]
	  heapify(arr, n, p)

def heapSort(arr, n):
  #build heap
  for i in range(n):
	  heapify(arr, n, i)

  for i in range(n-1, 0, -1):
	  arr[i], arr[0] = arr[0], arr[i]
	  # Heapify root element
	  heapify(arr, i, 0)


arr = [4, 12, 8, 9, 7, 5, 11]
heapSort(arr, len(arr))
print(arr)
  
