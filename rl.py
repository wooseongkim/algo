# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:32:59 2020

@author: Gachon
"""
import random

class myGrid:
    def __init__(self, n, m):
        self._x = 0
        self._y = 0
        self.max = (n, m)
        self.history = []
        self.data = [[0 for x in range(n+1)] for y in range(m+1)]
    def moveToEnd(self):
        self.history.append((0, 0))
        while 1:
            d = random.randint(0,3)
            if d == 0 and self._x < self.max[0]:                
                self._x += 1   
                self.data[self._x-1][self._y] = 0.999 * self.data[self._x-1][self._y] + 0.001 * (-1 + self.data[self._x][self._y])
                #self.history.append((self._x, self._y))
            elif d == 1 and self._x > 0:
                self._x -= 1
                self.data[self._x+1][self._y] = 0.999 * self.data[self._x+1][self._y] + 0.001 * (-1 + self.data[self._x][self._y])
                #self.history.append((self._x, self._y))
            elif d == 2 and self._y < self.max[1]:
                self._y += 1
                self.data[self._x][self._y-1] = 0.999 * self.data[self._x][self._y-1] + 0.001 * (-1 + self.data[self._x][self._y])
                #self.history.append((self._x, self._y))
            elif d == 3 and self._y > 0:
                self._y -= 1
                self.data[self._x][self._y+1] = 0.999 * self.data[self._x][self._y+1] + 0.001 * (-1 + self.data[self._x][self._y])
                #self.history.append((self._x, self._y))
            if (self._x, self._y) == self.max:
                break
        return self.history

for epoch in range(10):
    g = myGrid(3,3)
    h = g.moveToEnd()
        
#for epoch in range(50000):
#    g = myGrid(3,3)
#    h = g.moveToEnd()
#    #print(h)
#    reward  = 0
#    for i in h[::-1]:
#        data[i[0]][i[1]] = 0.999 * data[i[0]][i[1]] + 0.001 * reward
#        reward -= 1
#    for j in range(4):
#        print(data[j])
    
            