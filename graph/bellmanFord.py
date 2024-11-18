# calculates shortest distance from a starting point to all the points in the graph
# also detects negative cycles.
def bellmanFord(edges, n):
    # nodes starting with index 1
    distance = [float("inf") for _ in range(n)]

    # distance of starting node will be 0
    distance[0] = 0

    # check for every vertex
    # that would be n - 1 rounds
    # CAN BE OPTIMIZED

    for i in range(1, n):
        # start looking from nodee 1
        print("************")
        for edge in edges:
            fromVertex, toVertex, weight = edge[0] - 1, edge[1] - 1, edge[2]
            print(f"{fromVertex} -> {toVertex} -> {weight}")
            distance[toVertex] = min(distance[toVertex], distance[fromVertex] + weight)
        print(distance)

    cycle = False
    for fromEdge, toEdge, weight in edges:
        if distance[toEdge] < distance[fromEdge] + weight:
            cycle = True
            break

    print("No cycle found") if not cycle else print("Cycle Detected")

    print(distance)


# shortest path
# [from, to, weight]

edges = [(1, 2, 1), (2, 4, 1), (4, 3, -1), (1, 3, 4), (2, 5, 5), (4, 5, 4)]
n = 5
bellmanFord(edges, n)


# # negative cycle -> if there's a path with negative edge, if will keep getting shorter and shorter infinitely
# # Bellman Ford's algo helps detect such cycles.
# edges = [(1, 2, 3), (1, 3, 5), (2, 3, 2), (2, 4, 1), (3, 4, -7)]
# n = 4
# bellmanFord(edges, n)
