#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank: return -1
        queue = collections.deque([(start, 0)])
        while queue:
            gene, step = queue.popleft()
            if gene == end: return step
            for i in range(8):
                for c in "ACGT":
                    new_gene = gene[:i] + c + gene[i+1:]
                    if new_gene in bank:
                        bank.remove(new_gene)
                        queue.append((new_gene, step+1))
        return -1

# @lc code=end

