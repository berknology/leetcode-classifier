class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = collections.defaultdict(int)
        for num in nums:
            hash_table[num] += 1
            if hash_table[num] > 1:
                return True
        return False
