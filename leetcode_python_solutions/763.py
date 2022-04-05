class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        hash_table = dict()
        for i, c in enumerate(S):
            hash_table[c] = i
        ans = []
        last_index = 0
        cnt = 0
        for i, c in enumerate(S):
            cnt += 1
            last_index = max(last_index, hash_table[c])
            if i == last_index:
                ans.append(cnt)
                cnt = 0
        return ans
