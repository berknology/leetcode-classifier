#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        hash_table = dict()
        union_find = UnionFind(len(accounts))
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in hash_table:
                    hash_table[email] = i
                else:
                    union_find.union(i, hash_table[email])
                    hash_table[email] = union_find.find(i)
        
        unique_ids = set([union_find.find(i) for i in range(len(accounts))])
        ans = collections.defaultdict(list)
        for id in unique_ids:
            ans[id].append(accounts[id][0])
        emails = list(hash_table.keys())
        emails.sort()
        for email in emails:
            ans[union_find.find(hash_table[email])].append(email)
        return [ans[key] for key in ans]

# @lc code=end

