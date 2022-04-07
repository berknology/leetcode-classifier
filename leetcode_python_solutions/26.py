class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if len(nums) <= 1:
#             return len(nums)
#         index = 1
#         for i in range(1, len(nums)):
#             if nums[index - 1] != nums[i]:
#                 nums[index] = nums[i]
#                 index += 1
#
#         return index