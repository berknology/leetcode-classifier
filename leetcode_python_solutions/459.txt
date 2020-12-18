class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
            
        ss = (s + s)[1:-1]
        return s in ss

"""
abbcd abbcd


len(s)//i



"""
