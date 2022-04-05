class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        p1 = 0
        while p1 < len(haystack):
            if haystack[p1:p1+len(needle)] == needle:
                return p1
            p1 += 1
        return -1
