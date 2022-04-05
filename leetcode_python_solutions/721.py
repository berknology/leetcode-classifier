class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

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
        elif self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        else:
            self.rank[pu] += 1
            self.parent[pv] = pu
    

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        hash_table = dict()
        uf = UnionFind(n)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in hash_table:
                    hash_table[email] = i
                else:
                    uf.union(hash_table[email], i)
        parent_child_table = collections.defaultdict(list)
        for i in range(n):
            parent_child_table[uf.find(i)].append(i)
        ans = []
        for parent in parent_child_table:
            children = parent_child_table[parent]
            hash_set = set()
            for child in children:
                name =  accounts[child][0]
                emails = accounts[child][1:]
                for email in emails:
                    hash_set.add(email)
            email_list = list(hash_set)
            email_list.sort()
            acc = [name] + email_list
            ans.append(acc)
        return ans
        
        


    
        
"""
Union Find

Use a hash table with key email and value as the index of the account in the given list

Iterate through all list and emails, if an email exisit in the hash table, then do a union find

at the end of the day, we will know how much disjoint sets are there and return them

"""
