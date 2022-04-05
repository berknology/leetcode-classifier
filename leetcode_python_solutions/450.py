# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: 
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left or not root.right:
                return root.right or root.left
            else:
                node = root.left
                while node.right:
                    node = node.right
                root.val, node.val = node.val, root.val
                root.left = self.deleteNode(root.left, key)
        return root

