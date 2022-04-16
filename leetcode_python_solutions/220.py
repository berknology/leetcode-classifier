class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket = dict()
        for i, num in enumerate(nums):
            b = num // (t + 1)
            if b in bucket:
                return True
            if b - 1 in bucket and abs(bucket[b - 1] - num) <= t:
                return True
            if b + 1 in bucket and abs(bucket[b + 1] - num) <= t:
                return True

            bucket[b] = num
            if i - k >= 0:
                bucket.pop(nums[i - k] // (t + 1))
        return False