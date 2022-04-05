class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1
        up = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] and up != True:
                ans += 1
                up = True
            elif nums[i] < nums[i-1] and up != False:
                ans += 1
                up = False
        return ans
                

