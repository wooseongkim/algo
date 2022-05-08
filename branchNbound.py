# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:10:11 2020

@author: Gachon
"""
visited = [0 for i in range(5)]
G = [[0, 10, 10, 30, 25],\
     [10, 0, 14, 21, 10],\
     [10, 18, 0, 7, 9],\
     [8, 11, 7, 0, 3],\
     [14, 10, 10, 3, 0]]

root = 0
opt_path = 0
opt_cost = 10000
numV = 5  #number of vertices           
def dfs(v, path, cost):
    global G
    global opt_path
    global opt_cost
    global numV
    
    if len(path) > 0:
        cost += G[int(path[-1])][v]     
    path += str(v)
       
    #print(path, v, cost)
    for a in range(numV):
        if str(a) not in list(path):
            dfs(a, path, cost) 
            
    if len(path) == numV: 
        cost += G[int(path[-1])][0]
        if cost < opt_cost:
            opt_path = path+str(0)
            opt_cost = cost
            print('find a path ', opt_path, ' with ', opt_cost)
        return

dfs(0, "", 0)