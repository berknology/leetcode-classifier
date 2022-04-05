class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_bst(root, float('-inf'), float('inf'))
    def is_valid_bst(self, root, _min, _max):
        if not root: return True
        if root.val <= _min or root.val >= _max:
            return False
        return self.is_valid_bst(root.left, _min, root.val) and self.is_valid_bst(root.right, root.val, _max)
