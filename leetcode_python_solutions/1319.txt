class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return False
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
        return True
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        union_find = UnionFind(n)
        extra_conn = 0
        for conn in connections:
            if not union_find.union(conn[0], conn[1]):
                extra_conn += 1
        n_islands = len(set([union_find.find(i) for i in range(n)]))
        return n_islands - 1 if extra_conn >= n_islands-1 else -1 
    
