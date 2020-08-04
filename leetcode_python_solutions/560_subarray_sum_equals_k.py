class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = 0
        hash_table = collections.defaultdict(int)
        hash_table[0] += 1
        ans = 0
        for num in nums:
            cum_sum += num
            ans += hash_table[cum_sum - k]
            hash_table[cum_sum] += 1
        return ans


"""
Idea: use hash table and cumulative sum. Try similar problem Leetcode 437
Time complexity: O(n), where n is the length of nums
Space complexity: O(n)
"""