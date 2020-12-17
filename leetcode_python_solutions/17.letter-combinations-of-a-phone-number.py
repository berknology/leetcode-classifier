#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        self.ans = []
        self.backtrack(digits, [], 0)
        return self.ans

    def backtrack(self, digits, path, start):
        hash_map = {"2": "abc", 
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}
        n = len(digits)
        if start == n:
            self.ans.append(''.join(path))
            return

        for c in hash_map[digits[start]]:
            self.backtrack(digits, path+[c], start+1)
        
# @lc code=end

