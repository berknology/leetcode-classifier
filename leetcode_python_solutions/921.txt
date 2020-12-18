class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        hash_table = {"(": 1, ")": -1}
        n_open = n_close = 0
        for c in S:
            n_open += hash_table.get(c, 0)
            n_close += (n_open<0)
            n_open = max(n_open, 0)
        return n_open+n_close
        
