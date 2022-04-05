class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash_table = collections.defaultdict(int)
        ans = []
        for num in nums:
            hash_table[num] += 1
            if hash_table[num] > 1:
                ans.append(num)
        for i in range(1, len(nums)+1):
            if hash_table[i] == 0:
                ans.append(i)
        return ans
