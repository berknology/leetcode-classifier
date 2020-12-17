#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = collections.deque(preorder)
        return self.build_tree(preorder, inorder)

    def build_tree(self, preorder, inorder):
        if inorder:
            val = preorder.popleft()
            index = inorder.index(val)
            root = TreeNode(val)
            root.left = self.build_tree(preorder, inorder[:index])
            root.right = self.build_tree(preorder, inorder[index+1:])
            return root
# @lc code=end

