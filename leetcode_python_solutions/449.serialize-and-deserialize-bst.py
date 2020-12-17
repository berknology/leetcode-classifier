#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
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
        if not root: return ''
        data = []
        self.preorder(root, data)
        return ' '.join(data)
    
    def preorder(self, root, data):
        if not root: return
        data.append(str(root.val))
        self.preorder(root.left, data)
        self.preorder(root.right, data)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0: return None
        data = data.split()[::-1]
        return self.build_bst(data, float('-inf'), float('inf'))

    def build_bst(self, data, _min, _max):
        if data and _min < int(data[-1]) < _max:
            root = TreeNode(int(data.pop()))
            root.left = self.build_bst(data, _min, root.val)
            root.right = self.build_bst(data, root.val, _max)
            return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

