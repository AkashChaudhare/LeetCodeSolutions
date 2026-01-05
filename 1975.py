class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negatives = 0
        matrixsum = 0
        minelement = 10**6

        for row in matrix:
            for cell in row:
                if cell <0:
                    negatives+=1
                
                matrixsum += abs(cell)
                minelement = min(minelement, abs(cell))

        if negatives % 2 == 0:
            return matrixsum
        return matrixsum - 2*minelement
