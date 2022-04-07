class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            elif nums[slow] != 0:
                slow += 1
            fast += 1


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         index = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[index] = nums[i]
#                 index += 1
#         for i in range(index, len(nums)):
#             nums[i] = 0
