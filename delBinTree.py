# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:05:13 2020

@author: Gachon
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    n = Node(data)
                    n.parent = self
                    self.left = n
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    n = Node(data)
                    n.parent = self
                    self.right = n
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, val):
        if val < self.data:
            if self.left is None:
                return str(val)+" Not Found"
            return self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                return str(val)+" Not Found"
            return self.right.findval(val)
        else:            
            print(str(self.data) + ' is found')
            return self
    
    def swapMin(self, r):
        if self.right == None:
            if r.parent.data < r.data:
                r.parent.right = self
            else:
                r.parent.left = self
                
            self.right = r.right 
            self.left = r.left
            self.parent = r.parent
        else:
            self.right.swapMin(r)            
        
    def delVal(self):
        if self.right == None and self.left == None:
            if self.parent.data < self.data:
                self.parent.right = None
            else:
                self.parent.left = None
        elif self.right == None and self.left != None:
            print('case 2-1')
            if self.parent.data < self.data:
                self.parent.right = self.left
            else:
                self.parent.left = self.left
        elif self.right != None and self.left == None:
            print('case 2-2')
            if self.parent.data < self.data:
                self.parent.right = self.right
            else:
                self.parent.left = self.right
        else:
            print('case 3', self.right.data, self.left)
            self.swapMin(self)       
    
    def deleteValue(self, val):
        n = self.findval(val)
        n.delVal()
            
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

root = Node(30)
root.insert(20)
root.insert(25)
root.insert(40)
root.insert(10)
root.insert(25)
root.insert(35)
root.PrintTree()
print(root.findval(20))
root.deleteValue(20)
print(root.findval(20))
