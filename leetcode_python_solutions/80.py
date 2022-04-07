class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        flag = True
        slower, faster = 0, 1
        while faster <len(nums):
            if nums[slower] != nums[faster]:
                slower += 1
                nums[slower] = nums[faster]
                flag = True
            else:
                if flag:
                    slower += 1
                    nums[slower] = nums[faster]
                    flag = False
            faster += 1
        return slower + 1
