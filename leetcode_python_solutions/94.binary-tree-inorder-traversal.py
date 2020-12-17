#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            node = stack.pop()
            ans.append(node.val)
            current = node.right
        return ans

# @lc code=end

