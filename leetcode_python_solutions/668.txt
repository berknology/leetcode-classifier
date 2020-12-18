class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m*n
        while left < right:
            mid = left + (right-left)//2
            ans = 0
            for i in range(m):
                ans += min(mid//(i+1), n)
            if ans < k:
                left = mid +1 
            else:
                right = mid
        return left

        
"""
binary search



"""
