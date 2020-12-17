#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
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
        self.dfs(root, cum_sum = 0, target = sum)
        return self.ans

    def dfs(self, root, cum_sum, target):
        if not root: return
        cum_sum += root.val
        self.ans += self.hash_table[cum_sum-target]
        self.hash_table[cum_sum] += 1
        self.dfs(root.left, cum_sum, target)
        self.dfs(root.right, cum_sum, target)
        self.hash_table[cum_sum] -= 1

# @lc code=end

