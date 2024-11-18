from collections import deque


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Bellman Ford
        # distance = [float('inf') for _ in range(n)]
        # distance[k - 1] = 0

        # for i in range(n-1):
        #     distanceChanged = False
        #     for fromEdge, toEdge, weight in times:
        #         if distance[toEdge - 1] > distance[fromEdge - 1] + weight:
        #             distance[toEdge - 1] = distance[fromEdge - 1] + weight
        #             distanceChanged = True
        #     if distanceChanged == False:
        #         break

        # return -1 if max(distance) == float('inf') else max(distance)

        # BFS
        distance = [float("inf") for _ in range(n)]

        distance[k - 1] = 0

        queue = deque()
        queue.append([0, k - 1])

        adjacencyList = [[] for _ in range(n)]
        for fromNode, toNode, weight in times:
            adjacencyList[fromNode - 1].append((weight, toNode - 1))

        while queue:
            head = queue.popleft()
            dist, current = head
            for d, t in adjacencyList[current]:
                if distance[t] > distance[current] + d:
                    distance[t] = distance[current] + d
                    queue.append([distance[t], t])

        maxTime = max(distance)
        return -1 if maxTime == float("inf") else maxTime
