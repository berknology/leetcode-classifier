class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        ans = []
        for i in range(n):
            cur = intervals[i]
            if cur[1] < newInterval[0]:
                ans.append(cur)
            elif cur[0] > newInterval[1]:
                ans.append(newInterval)
                ans.extend(intervals[i:])
                return ans
            else:
                newInterval = [min(cur[0], newInterval[0]), max(cur[1], newInterval[1])]
        ans.append(newInterval)
        return ans
    
    
"""
1. xxxxxx
            xxxx    
            
2.  xxxxxx
       xxxx
      
3.       xxxxxx
    xxx

"""
