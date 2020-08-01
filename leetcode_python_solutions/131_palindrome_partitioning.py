class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.backtrack(s, 0, [], ans)
        return ans

    def backtrack(self, s, index, path, ans):
        if index == len(s):
            ans.append(path)
            return
        for i in range(index, len(s)):
            sub_str = s[index:i+1]
            if sub_str[::-1] != sub_str:
                continue
            self.backtrack(s, i+1, path+[sub_str], ans)


"""
Time complexity: O(2^n), where n is the length of the string.
Space complexity: O(n). We need to consider the implicit stack used in recursion
"""