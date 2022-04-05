class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_table = dict()
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                idx = stack.pop()
                hash_table[nums2[idx]] = nums2[i]
            stack.append(i)
        for i in range(len(nums1)):
            nums1[i] = hash_table.get(nums1[i], -1)  
        return nums1
