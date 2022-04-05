class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.top_down(strs, len(strs)-1, m, n, {})
    
    def top_down(self, strs, index, i, j, memo):
        if (i == 0 and j == 0) or index < 0:
            return 0
        if (i, j, index) in memo:
            return memo[(i, j, index)]
        string = strs[index]
        n_zeros = string.count('0')
        n_ones = string.count('1')
        if n_zeros <= i and n_ones <= j:
            include = 1 + self.top_down(strs, index-1, i-n_zeros, j-n_ones, memo)
            not_include = self.top_down(strs, index-1, i, j, memo)
            ans = max(include, not_include)
        else:
            ans = self.top_down(strs, index-1, i, j, memo)
        memo[(i, j, index)] = ans
        return ans
    
        

"""
DP

memo[(i, j, index)] with i zeros and j ones


"""
