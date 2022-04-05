class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        left_max = float('-inf')
        for i, num in enumerate(arr):
            left_max = max(left_max, num)
            if i >= left_max:
                ans += 1
        return ans
