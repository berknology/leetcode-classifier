#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#

# @lc code=start

class UnionFind:
    def __init__(self, n):
        self._parents = [i for i in range(n)]
        self._ranks = [1 for _ in range(n)]
    
    def find(self, u):
        if u != self._parents[u]:
            self._parents[u] = self.find(self._parents[u])
        return self._parents[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:        
            self._parents[pv] = pu
            self._ranks[pu] += 1
        return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        union_find = UnionFind(26)
        check_later = []
        for equ in equations:
            if equ[1] == '!':
                check_later.append(equ)
            else:
                n1 = ord(equ[0])-ord('a')
                n2 = ord(equ[-1])-ord('a')
                _ = union_find.union(n1, n2)
        for equ in check_later:
            n1 = ord(equ[0])-ord('a')
            n2 = ord(equ[-1])-ord('a')
            p1 = union_find.find(n1)
            p2 = union_find.find(n2)
            if p1 == p2:
                return False
        return True

# @lc code=end

