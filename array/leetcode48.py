class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # diagonal flip
        for i in range(ROWS):
            for j in range(i+1, COLS):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # vertical flip
        for row in matrix:
            row.reverse()