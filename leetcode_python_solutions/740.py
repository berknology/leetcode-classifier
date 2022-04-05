class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        _min, _max = min(nums), max(nums)
        cnt = collections.Counter(nums)
        if len(cnt) == 1:
            return _min*cnt[_min]
        dp = [0]*(_max-_min+1)
        dp[0] = _min*cnt[_min]
        dp[1] = max(_min*cnt[_min], (_min+1)*cnt[_min+1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2]+(_min+i)*cnt[(_min+i)])
        return max(dp)

