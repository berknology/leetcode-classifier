class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        deg = max(cnt.values())
        start = dict()
        end = dict()
        for i, num in enumerate(nums):
            if num not in start:
                start[num] = i
            end[num] = i
        length = float('inf')
        for key in cnt:
            if cnt[key] == deg:
                length = min(length, end[key]-start[key]+1)
        return length
