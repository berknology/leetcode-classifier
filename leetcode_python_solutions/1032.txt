class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        check_later = []
        for e in equations:
            if e[1] == '=':
                uf.union(ord(e[0])- ord('a'), ord(e[-1])- ord('a'))
            else:
                check_later.append(e)
        for ie in check_later:
            p0, p1 = uf.find(ord(ie[0])- ord('a')), uf.find(ord(ie[-1])- ord('a'))
            if p0 == p1:
                return False
        return True

    
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
        
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        else:
            self.rank[pv] += 1
            self.parent[pu] = pv
        return True
