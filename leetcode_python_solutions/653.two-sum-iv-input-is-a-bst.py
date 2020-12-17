#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        inorder = []
        self.dfs(root, inorder)
        left, right = 0, len(inorder)-1
        while left < right:
            _sum = inorder[left] + inorder[right]
            if _sum == k:
                return True
            elif _sum < k:
                left += 1
            else:
                right -= 1
        return False
    
    def dfs(self, root, inorder):
        if not root: return
        self.dfs(root.left, inorder)
        inorder.append(root.val)
        self.dfs(root.right, inorder)
    

# @lc code=end

