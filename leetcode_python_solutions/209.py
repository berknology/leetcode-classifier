class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = float('inf')
        cur_sum = 0
        p1 = p2 = 0
        while p2 < len(nums):
            if cur_sum + nums[p2] >= s:
                ans = min(ans, p2-p1+1)
                cur_sum -= nums[p1]
                p1 += 1
            else:
                cur_sum += nums[p2]
                p2 += 1
        return ans if ans != float('inf') else 0
