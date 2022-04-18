# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = TreeNode(None)
        self.cur = self.ans

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.inorder(root)
        return self.ans.right

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.cur.right = root
        root.left = None
        self.cur = root
        self.inorder(root.right)
