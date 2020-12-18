class Solution:
    def minSteps(self, n: int) -> int:
        if n <= 1:
            return 0
        elif n == 2:
            return 2
        ans = n
        for i in range(2, int(n//2)+1):
            if n%i == 0:
                ans = min(ans, i+self.minSteps(n//i))
        return ans
    
        
"""
3
copy
paste
paste


4
copy
paste
copy
paste


5
copy
paste
paste
paste
paste


6
copy
paste
copy
paste
paste
"""
