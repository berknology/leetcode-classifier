class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.backtrack(s, path=[], start=0)
        return self.ans
    
    def backtrack(self, s, path, start):
        if start == len(s):
            self.ans.append(path)
            return
        for i in range(start, len(s)):
            sub_str = s[start:i+1]
            if sub_str == sub_str[::-1]:
                self.backtrack(s, path+[sub_str], i+1)
