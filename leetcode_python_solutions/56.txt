class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if cur[-1] < intervals[i][0]:
                ans.append(cur)
                cur = intervals[i]
            else:
                cur[-1] = max(cur[-1], intervals[i][-1])
        ans.append(cur)
        return ans
    
    
"""
[[1,3],[2,6],[8,10],[15,18]]
cur [1, 6]


xxxxxxxxxxx
       xxxxxxxxxxxx
       
       
xxxxxxxxxxx
    xxxx
    
       

"""
