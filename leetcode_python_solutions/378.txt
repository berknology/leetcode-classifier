class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + (right-left)//2
            n = sum([bisect.bisect(row, mid) for row in matrix])
            if n < k:
                left = mid +1
            else:
                right = mid
        return left

        
"""
Approach 1: binary search
Approach 2: heap

"""
