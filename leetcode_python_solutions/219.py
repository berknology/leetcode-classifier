class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if hash_table[num] > 0:
                return True
            hash_table[num] += 1
            if i - k >= 0:
                hash_table[nums[i-k]] -= 1
        return False