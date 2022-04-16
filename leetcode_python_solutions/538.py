# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.sum = 0
        root = self.convert_to_bst(root)
        return root

    def convert_to_bst(self, root):
        if not root:
            return None
        self.convert_to_bst(root.right)
        self.sum += root.val
        root.val = self.sum
        self.convert_to_bst(root.left)
        return root