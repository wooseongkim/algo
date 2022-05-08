# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:51:30 2020

@author: Gachon
"""
topo ={(1,2):8, (1,3):11, (1,4):9, (2,5):10, (3,4):13, (4,5):5, \
    (3,6):8, (6,7):7, (4,7):12}

def adjVertex(n):
    adj = []
    global topo
    for e in topo.keys():
        if e[0] == n:
            adj.append(e[1])
    return adj

def delMin(Q, d):
    minVal = 10000
    minNode = 0
    for i in Q:
        if d[i] < minVal:
            minVal = d[i]
            minNode = i
    Q.remove(minNode)
    return minNode

d = [10000 for x in range(0,8)]
d[1] = 0
Q = list(range(1,8))
tree = list(range(0,8))
while Q:
    u = delMin(Q, d)
    for v in adjVertex(u):
        if v in Q and topo[(u,v)] < d[v]:
            d[v] = topo[(u,v)]
            tree[v] = u
print(d)
print(tree)