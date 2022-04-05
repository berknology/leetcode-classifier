class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
        
"""
cycle detection
slow and fast pointers


index   [0, 1, 2, 3, 4]
value   [1, 3, 4, 2, 2]

0 -> 1 -> 3 ->  2  -> 4
                ^     |
                |     |
                ------   
"""
