# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.n1 = self.n2 = None
        self.pre = None
        self.inorder(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.n1:
                self.n1 = self.pre
            self.n2 = root
        self.pre = root
        self.inorder(root.right)
        

