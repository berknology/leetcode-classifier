import collections
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hash_table = collections.defaultdict(int)
        for num in arr:
            hash_table[num] = hash_table[num-difference] + 1
        return max(hash_table.values())
