class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cum_sum = 0
        hash_table = collections.defaultdict(int)
        hash_table[0] = 1
        for num in nums:
            cum_sum += num
            ans += hash_table[cum_sum-k]
            hash_table[cum_sum] += 1
        return ans
        
