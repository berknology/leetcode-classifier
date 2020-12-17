#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return []
        data = []
        self.preorder(root, data)
        return ','.join(data)

    def preorder(self, root, ans):
        if not root: 
            ans.append('null')
            return
        ans.append(str(root.val))
        self.preorder(root.left, ans)
        self.preorder(root.right, ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0: return None
        data = data.split(',')[::-1]
        return self.build_tree(data)
    
    def build_tree(self, data):
        if not data: return
        if data[-1] != 'null':
            root = TreeNode(int(data.pop()))
            root.left = self.build_tree(data)
            root.right = self.build_tree(data)
            return root
        else:
            data.pop()
            return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

