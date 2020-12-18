# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        pre = []
        self.preorder(root, pre)
        return ' '.join(pre)
    
    def preorder(self, root, pre):
        if not root:
            return 
        pre.append(str(root.val))
        self.preorder(root.left, pre)
        self.preorder(root.right, pre)
        
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        pre = data.split(' ')[::-1]
        return self.construct_bst(pre, float('-inf'), float('inf'))
    
    def construct_bst(self, pre, lower, upper):
        if not pre:
            return None
        if lower < int(pre[-1]) < upper:
            root = TreeNode(int(pre.pop()))
            root.left = self.construct_bst(pre, lower, root.val)
            root.right = self.construct_bst(pre, root.val, upper)
            return root
        else:
            return None
        
"""
Leverage preorder and the algo to recontruct a BST using preorder
"""

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
