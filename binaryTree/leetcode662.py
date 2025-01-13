# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        currentLevel = deque([[root, 1]])
        nextLevel = deque()
        firstIndex = 0
        while currentLevel:

            currentNode, index = currentLevel.popleft()
            
            if not firstIndex:
                firstIndex = index

            if currentNode.left:
                nextLevel.append([currentNode.left, index * 2])
            if currentNode.right:
                nextLevel.append([currentNode.right, ( index * 2 ) + 1])
            
            if not currentLevel:
                # new level starts
                
                res = max(res, index - firstIndex + 1)
                
                firstIndex = 0
                currentLevel = nextLevel
                nextLevel = deque()

        return res