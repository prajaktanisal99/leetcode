from typing import List
from collections import deque
# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def topView(root: BinaryTreeNode) -> List[int]:
    # Write your code here.
    indexDic = {}

    if not root:
        return []
    
    queue = deque([[root, 0]])
    while queue:
        currentNode, index = queue.popleft()
        
        if index not in indexDic:
            indexDic[index] = currentNode.data

        if currentNode.left:
            queue.append([currentNode.left, index - 1])
        if currentNode.right:
            queue.append([currentNode.right, index + 1])
    
    indexDic = [indexDic[i] for i in sorted(indexDic)]
    print(indexDic)

root = BinaryTreeNode(2, BinaryTreeNode(7, BinaryTreeNode(2, None, None), BinaryTreeNode(6, BinaryTreeNode(5, None, None), BinaryTreeNode(11, None, None))), BinaryTreeNode(5, None, BinaryTreeNode(9, BinaryTreeNode(4, None, None), None)))

topView(root)