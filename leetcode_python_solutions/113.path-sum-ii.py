#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.ans = []
        self.dfs(root, sum, [])
        return self.ans

    def dfs(self, root, sum, path):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and root.val == sum:
            self.ans.append(path[:])
        else:
            self.dfs(root.left, sum-root.val, path)
            self.dfs(root.right, sum-root.val, path)
        path.pop()
        
# @lc code=end

