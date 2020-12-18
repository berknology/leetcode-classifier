from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        ans = []
        min_len = min([len(str) for str in strs])
        for pnt in range(min_len):
            c = strs[0][pnt]
            if all([c == str[pnt] for str in strs]):
                ans.append(c)
            else:
                break
        return ''.join(ans)
