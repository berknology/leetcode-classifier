#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        return self.generate_bst(1, n)
    
    def generate_bst(self, left, right):
        if right < left:
            return [None]
        else:
            res = []
            for i in range(left, right+1):
                left_tree = self.generate_bst(left, i-1)
                right_tree = self.generate_bst(i+1, right)
                for l in left_tree:
                    for r in right_tree:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

# @lc code=end

