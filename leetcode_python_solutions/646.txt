class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if len(pairs) == 1:
            return 1
        pairs.sort(key=lambda x: x[-1])
        p1 = 0
        p2 = 1
        ans = 1
        while p2 < len(pairs):
            if pairs[p1][-1] < pairs[p2][0]:
                ans += 1
                p1 = p2
            p2 += 1
        return ans

    
"""
xxxxxxxx
     xxxxxxx
   xxxxxxxxxxxxx  


"""
                
