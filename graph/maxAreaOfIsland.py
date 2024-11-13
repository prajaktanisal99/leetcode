class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
                grid[r][c] = 0
                return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            else:
                return 0

        maxCount = 0
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 1:
                    maxCount = max(maxCount, dfs(r, c))

        return maxCount
