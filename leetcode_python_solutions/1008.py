# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        preorder.reverse()
        return self.construct_bst(preorder, float('-inf'), float('inf'))

    def construct_bst(self, preorder, lower, upper):
        if not preorder:
            return None
        if lower < preorder[-1] < upper:
            root = TreeNode(preorder.pop())
            root.left = self.construct_bst(preorder, lower, root.val)
            root.right = self.construct_bst(preorder, root.val, upper)
            return root
