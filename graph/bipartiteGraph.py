from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = ["g" for _ in range(len(graph))]

        for i in range(len(graph)):
            if color[i] != "g":
                continue

            queue = deque([i])
            color[i] = "b"

            while queue:
                head = queue.popleft()
                for v in graph[head]:
                    if color[v] == "g":
                        color[v] = "r" if color[head] == "b" else "b"
                        queue.append(v)
                    elif color[head] == color[v]:
                        return False
        return True
