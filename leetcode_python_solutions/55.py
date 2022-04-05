class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end_index = nums[0]
        index = 0
        while index <= end_index:
            end_index = max(end_index, index+nums[index])
            if end_index >= len(nums)-1:
                return True
            index += 1
        return end_index >= len(nums)-1


