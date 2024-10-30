#binary tree search
#this is a test of the implementaiton of the the binary tree search

import random as r 

class BinarySearchTree():
    def __init__(self,node):
        self.node = node
        self.left = None
        self.right = None

    def insert(self,node):
        if node < self.node:
            if self.left is None:
                self.left = BinarySearchTree(node)
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = BinarySearchTree(node)
            else:
                self.right.insert(node)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.node)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.node)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()


    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.node)

    
    def find(self,node):
        if node < self.node:
            if self.left == None:
                return False
            else:
                return self.left.find(node)
        elif node > self.node:
            if self.right == None:
                return False
            else:
                return self.right.find(node)
        else:
            return True
        

inserter = BinarySearchTree(6)

inserter.insert(5)
inserter.insert(4)
inserter.insert(1)
inserter.insert(8)
inserter.insert(9)
inserter.insert(12)
inserter.insert(17)
inserter.insert(2)
inserter.insert(17)
inserter.insert(56)
inserter.insert(42)

print(inserter.find(2))
print(inserter.find(62))
print(inserter.find(8))
print(inserter.left.node)

