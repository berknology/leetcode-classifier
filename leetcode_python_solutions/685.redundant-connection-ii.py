#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#

# @lc code=start

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return False
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True
        

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges))
        cand1, cand2, point_to = None, None, dict()
        for node1, node2 in edges:
            if node2 in point_to:
                cand1, cand2 = point_to[node2], [node1, node2]
                break
            point_to[node2] = [node1, node2]
            
        for node1, node2 in edges:
            if [node1, node2] == cand2: continue
            if not union_find.union(node1 - 1, node2 - 1):
                if cand1: return cand1
                return [node1, node2]
        return cand2

# @lc code=end

