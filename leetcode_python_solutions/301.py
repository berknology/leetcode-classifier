class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n_open, n_close = self.calculate_imbalance(s)
        self.ans = []
        self.backtrack(s, n_open, n_close, 0)
        return self.ans
    
    def backtrack(self, s, n_open, n_close, start):
        if n_open == 0 and n_close == 0:
            self.ans.append(s)
            return
        for i in range(start, len(s)):
            if i > start and s[i] == s[i-1]: continue
            if s[i] in "()":
                new_s = s[:i] + s[i+1:]
                n_open_new, n_close_new = self.calculate_imbalance(new_s)
                if s[i] == '(' and n_open_new < n_open and n_close_new <= n_close:
                    self.backtrack(new_s, n_open_new, n_close_new, i)
                elif s[i] == ')' and n_open_new <= n_open and n_close_new < n_close:
                    self.backtrack(new_s, n_open_new, n_close_new, i)

    def calculate_imbalance(self, s):
        n_open = n_close = 0
        hash_table = {"(": 1, ")": -1}
        for c in s:
            n_open += hash_table.get(c, 0)
            n_close += (n_open < 0)
            n_open = max(n_open, 0)
        return n_open, n_close
