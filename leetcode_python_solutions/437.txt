# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.hash_table = collections.defaultdict(int)
        self.hash_table[0] += 1
        self.ans = 0
        self.dfs(root, sum, 0)
        return self.ans
    
    def dfs(self, root, sum, cur_sum):
        if not root:
            return
        cur_sum += root.val
        self.ans += self.hash_table[cur_sum-sum]
        self.hash_table[cur_sum] += 1
        self.dfs(root.left, sum, cur_sum)
        self.dfs(root.right, sum, cur_sum)
        self.hash_table[cur_sum] -= 1
        
    
