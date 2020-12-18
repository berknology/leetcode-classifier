class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: 
            return False
        return self.is_same_tree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    def is_same_tree(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        else:
            if s.val != t.val:
                return False
            else:
                return self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right)
