class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n
        while left < right:
            mid = left + (right-left)//2
            r, c = mid//n, mid%n
            if matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid
        if left == m*n or matrix[left//n][left%n] != target:
            return False
        else:
            return True
            
