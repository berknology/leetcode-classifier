class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash_s = collections.Counter(s[:len(p)-1])
        hash_p = collections.Counter(p)
        ans = []
        for i in range(len(p)-1, len(s)):
            hash_s[s[i]] += 1
            if hash_s == hash_p:
                ans.append(i-len(p)+1)
            hash_s[s[i-len(p)+1]] -= 1
            if hash_s[s[i-len(p)+1]] == 0:
                del hash_s[s[i-len(p)+1]]
        return ans
        
"""
hash_table + sliding window

"""
