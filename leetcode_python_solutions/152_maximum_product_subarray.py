class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = 1
        cur_max = 1
        max_prod = float('-inf')
        for num in nums:
            cur_min, cur_max = min(num, cur_min*num, cur_max*num), max(num, cur_min*num, cur_max*num)
            max_prod = max(max_prod, cur_max)
        return max_prod


"""
Time complexity: O(n) where n is the length of `nums` array
Space complexity: O(1)
"""