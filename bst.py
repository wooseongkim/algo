# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 22:00:33 2022

@author: Gachon
"""

class Node:
    def __init__(self, k):
        self.key = k
        self.right = []
        self.left = []
        self.parent = []

class BST:
    def __init__(self):
        self.root = []
    def insert(self, r, n, p):
        if not r:
            n.parent.append(p)
            r.append(n)
            return r
        if r[0].key > n.key:
            self.insert(r[0].left, n, r[0])
        else:
            self.insert(r[0].right, n, r[0])
    def search(self, r, _key):
        if r[0].key == _key:
            print('found ', r[0].key)
            return r[0]
        if r[0].key > _key:
            return self.search(r[0].left, _key)
        else:
            return self.search(r[0].right, _key)
    def delete(self, t, r):
    	if r == t:
            self.root =[]
            self.root.append(deleteNode(t))# r == root   
    	elif r == r.parent[0].left[0]:
            r.parent[0].left = []
            r.parent[0].left.append(deleteNode(r))# r is p's left child 
    	else:
            r.parent[0].right = []
            r.parent[0].right.append(deleteNode(r))# r is p's right child  

    def deleteNode(self, r):       
            if not r.left and not r.right:
                return None#case 1
            elif not r.left and r.right:
                return r.right#case 2-1 
            elif r.left and not r.right:
                return r.left#Case 2-2 
            else:#Case 3 
    		s = r.right[0]
            parent = s
    		while s.left[s]:
                parent = s;  s=s.left[s]
    		key[r] ← key[s]; 
    		if (s = right[r]) then right[r] ← right[s];
    			   else left[parent] ← right[s];
    		return r;


        
tr = BST()
a = Node(6); b= Node(9); c = Node(2); d=Node(3); e=Node(7); f=Node(1)
tr.insert(tr.root, a, tr.root)
tr.insert(tr.root, b, tr.root)
tr.insert(tr.root, c, tr.root)
tr.insert(tr.root, d, tr.root)
tr.insert(tr.root, e, tr.root)
tr.insert(tr.root, f, tr.root)
print(c.right[0].key, c.left[0].key, c.parent[0].key)
print('search ', tr.search(tr.root, 7).key)
        
        