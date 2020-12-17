#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) == 0 or len(s) > 12:
            return []
        self.ans = []
        self.backtrack(s, path=[], start=0)
        return self.ans

    def backtrack(self, s, path, start):
        if start == len(s) and len(path) == 4:
            self.ans.append('.'.join(path))
            return
        for i in range(start, len(s)):
            sub_str = s[start:i+1]
            if int(sub_str) > 255 or len(sub_str) > 1 and sub_str[0] == '0':
                break
            self.backtrack(s, path+[sub_str], i+1)

# @lc code=end

