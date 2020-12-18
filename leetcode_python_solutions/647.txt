class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += self.expand(s, i, i)
            ans += self.expand(s, i-1, i)
        return ans
    def expand(self, s, i, j):
        ans = 0
        while 0 <= i < len(s) and 0 <= j < len(s):
            if s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1
            else:
                break
        return ans
