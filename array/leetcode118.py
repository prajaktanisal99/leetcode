class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]
        for i in range(1, numRows):
            prevRow = res[i-1]
            currentRow = [1]
            for j in range(1, i):
                currentRow.append(prevRow[j-1] + prevRow[j])
            currentRow.append(1)
            res.append(currentRow)
        
        return res