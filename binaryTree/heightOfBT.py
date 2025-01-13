def height(root):
    # Write your code here.
    
    stack = []
    height = 0

    def dfs(node):
        nonlocal height
        if node:
            stack.append(node.data)
        
        if not node.left and not node.right:
            height = max(height, len(stack))
            
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
        stack.pop()

    dfs(root)
    print(f'Height::{height}')


class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right

root = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4, None, None), BinaryTreeNode(5, BinaryTreeNode(6, None, None), BinaryTreeNode(7, None, None))), BinaryTreeNode(3, None, None))

height(root)