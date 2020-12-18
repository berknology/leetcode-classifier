class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_table_s = dict()
        hash_table_t = dict()
        for i in range(len(s)):
            if s[i] not in hash_table_s:
                hash_table_s[s[i]] = t[i]
            else:
                if hash_table_s[s[i]] != t[i]:
                    return False
            if t[i] not in hash_table_t:
                hash_table_t[t[i]] = s[i]
            else:
                if hash_table_t[t[i]] != s[i]:
                    return False
        return True
