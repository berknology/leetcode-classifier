class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s: return 0
        g.sort()
        s.sort()
        pnt1 = 0
        pnt2 = 0
        while pnt1 < len(g) and pnt2 < len(s):
            if s[pnt2] >= g[pnt1]:
                pnt1 += 1
            pnt2 += 1
        return pnt1
