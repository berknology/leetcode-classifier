class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = self.find_smallest_index(nums)
        l = self.find_largest_index(nums)
        return l-s+1 if l >= s else 0
    
    def find_smallest_index(self, nums):
        stack = []
        index = len(nums)
        for i, num in enumerate(nums):
            while stack and num < nums[stack[-1]]:
                index = min(index, stack.pop())
            stack.append(i)
        return index
    
    def find_largest_index(self, nums):
        stack = []
        index = len(nums)
        nums = nums[::-1]
        for i, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                index = min(index, stack.pop())
            stack.append(i)
        return len(nums)-1-index
