class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = 0
        r = nums[0]
        steps = 1
        while r < len(nums)-1:
            steps += 1
            can_reach = max(i + nums[i] for i in range(l, r + 1))
            l, r = r+1, can_reach 
        return steps

