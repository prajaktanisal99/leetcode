"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        if not node:
            return None

        queue = deque([node])

        clonedNodes = {node: Node(node.val)}
        # queue.append(node)
        while queue:

            current = queue.popleft()

            for n in current.neighbors:

                if n not in clonedNodes:
                    clonedNodes[n] = Node(n.val)
                    queue.append(n)

                clonedNodes[current].neighbors.append(clonedNodes[n])

        return clonedNodes[node]
