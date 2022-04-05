class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = collections.Counter(nums)
        if k == 0:
            return sum([cnt[key] > 1 for key in cnt])
        else:
            return sum([i+k in cnt for i in cnt])

