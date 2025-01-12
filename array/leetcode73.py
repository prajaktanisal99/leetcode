class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        points = []
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    points.append([i, j])

        # we have [r,c] for all 0
        # print(points)

        for point in points:
            r, c = point 
        
            # update all columns for rth row
            for j in range(COLS):
                matrix[r][j] = 0 

            # update all rows for cth column 
            for i in range(ROWS):
                matrix[i][c] = 0 