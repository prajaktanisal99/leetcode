# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        res = []
        currentLevel = deque([root])
        nextLevel = deque()

        while currentLevel:
            currentNode = currentLevel.popleft()
            print(currentNode)
            if currentNode.left:
                nextLevel.append(currentNode.left)
            if currentNode.right:
                nextLevel.append(currentNode.right)
            
            if not currentLevel:
                res.append(currentNode. val)
                currentLevel = nextLevel
                nextLevel = deque()
        
        return res