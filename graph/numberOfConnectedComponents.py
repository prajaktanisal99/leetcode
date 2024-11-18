def countComponents(n, edges):

    connected = n
    size = [1 for _ in range(n)]
    parent = [i for i in range(n)]

    def find(n):
        while n != parent[n]:
            n = parent[n]

        return n

    def union(n1, n2):
        nonlocal connected
        parent1, parent2 = find(n1), find(n2)
        newParent = min(parent1, parent2)
        if parent1 == parent2:
            return 0

        parent[n1] = newParent
        parent[n2] = newParent
        return 1

    for edge in edges:
        connected -= union(edge[0], edge[1])

    print(connected)


countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]])
"""
Expected : 2
"""

countComponents(3, [[0, 1], [0, 2]])
"""
Expected : 1
"""
