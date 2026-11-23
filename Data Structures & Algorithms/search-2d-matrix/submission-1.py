class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        w, h = len(matrix[0]), len(matrix)
        s, b = 0, w * h

        while s < b:
            m = s + ((b-s)//2)
            i,j = m // w, m % w
            if matrix[i][j] < target:
                s = m+1
            elif matrix[i][j] > target:
                b = m
            else:
                return True
        return False

