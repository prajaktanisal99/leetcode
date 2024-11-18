class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        lenEdges = len(edges) + 1
        parent = [i for i in range(len(edges))]
        size = [1] * lenEdges
        cycle = []

        def find(node):
            while node != parent[node]:
                node = parent[node]
            return node

        def unionBySize(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return [a + 1, b + 1]

            if size[rootA] > size[rootB]:
                parent[rootB] = rootA
                size[rootA] += size[rootB]
            else:
                parent[rootA] = rootB
                size[rootB] += size[rootA]

            return

        for edge in edges:
            res = unionBySize(edge[0] - 1, edge[1] - 1)
            if res:
                return res

        return []
