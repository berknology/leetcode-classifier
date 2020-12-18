class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        max_len = 0
        for num in nums:
            if num+1 in cnt:
                max_len = max(max_len, cnt[num]+cnt[num+1])
        return max_len

