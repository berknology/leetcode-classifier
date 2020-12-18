class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_len = 1
        for num in num_set:
            if num - 1 not in num_set:
                cur_len = 1
                while num + 1 in num_set:
                    cur_len += 1
                    num += 1
                max_len = max(max_len, cur_len)
        return max_len

