class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
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

