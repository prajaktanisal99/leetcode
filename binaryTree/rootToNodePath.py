'''
    Following is the class structure of the BinaryTreeNode class:

    

'''
from typing import List
class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right

def rootToNode(root, target):
    # Write your code here.

    stack = []

    def dfs(node):
        if node:
            stack.append(node.data)
        if node.data == target:
            print(stack)
            return
        
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
        stack.pop()

    dfs(root)

def rootToAllLeaf(root):
    # Write your code here.
    
    stack = []

    def dfs(node):
        if node:
            stack.append(node.data)
        
        if not node.left and not node.right:
            print(stack)
            
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
        stack.pop()

    dfs(root)

root = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4, None, None), BinaryTreeNode(5, BinaryTreeNode(6, None, None), BinaryTreeNode(7, None, None))), BinaryTreeNode(3, None, None))

rootToNode(root, 7)
rootToAllLeaf(root)