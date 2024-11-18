from collections import deque


def islandsAndTreasure(grid):

    ROWS = len(grid)
    COLS = len(grid[0])

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                queue = deque()
                queue.append([r, c])
                distance = 1
                child = deque()
                while queue:
                    currentR, currentC = queue.popleft()

                    if 0 <= currentR - 1 and grid[currentR - 1][currentC] > distance:
                        grid[currentR - 1][currentC] = distance
                        child.append([currentR - 1, currentC])

                    if 0 <= currentC - 1 and grid[currentR][currentC - 1] > distance:
                        grid[currentR][currentC - 1] = distance
                        child.append([currentR, currentC - 1])

                    if currentR + 1 < ROWS and grid[currentR + 1][currentC] > distance:
                        grid[currentR + 1][currentC] = distance
                        child.append([currentR + 1, currentC])

                    if currentC + 1 < COLS and grid[currentR][currentC + 1] > distance:
                        grid[currentR][currentC + 1] = distance
                        child.append([currentR, currentC + 1])

                    if not queue:
                        queue = child
                        child = deque()
                        distance += 1

    print("----------------------")
    for row in grid:
        print(row)


"""
Expected:
[
  [0,-1],
  [1,2]
]
"""

islandsAndTreasure([[0, -1], [2147483647, 2147483647]])

print("**********************")
islandsAndTreasure(
    [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
)

"""
Expected
 [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
"""
