class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        islandSize = {}
        islandMap = {}
        waterCells = []
        n = len(grid)

        def dfs(i, j, parent):

            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] == 0:
                return 0

            if (i, j) in visited:
                return 0

            visited.add((i, j))
            islandMap[(i, j)] = parent
            size = 1

            size += dfs(i - 1, j, parent)  
            size += dfs(i + 1, j, parent)  
            size += dfs(i, j - 1, parent)  
            size += dfs(i, j + 1, parent)  
            
            return size

        res = 0

        
        for i in range(n):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 1:
                    size = dfs(i, j, (i, j))
                    res = max(res, size)
                    islandSize[(i, j)] = size
                elif grid[i][j] == 0:
                    waterCells.append((i, j))

        for i, j in waterCells:
            
            curMax = 0
            uniqueParents = []
            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
            
                if (x, y) in islandMap:
                    parent = islandMap[(x, y)]
            
                    if parent not in uniqueParents:
                        uniqueParents.append(parent)
                        curMax += islandSize[parent]

            res = max(curMax + 1, res)

        return res