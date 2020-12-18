class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            two_sum_ans = self.two_sum(nums, i, -num)
            for res in two_sum_ans:
                ans.append([num, res[0], res[1]])
        return ans
    
    def two_sum(self, nums, index, target):
        res = []
        left, right = index+1, len(nums)-1
        while left < right:
            _sum = nums[left] + nums[right]
            if _sum == target:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif _sum < target:
                left += 1
            else:
                right -= 1
        return res

        
"""
unique tiplets

naive solution: O(n^3)

Optimized solution: O(n^2)

"""
