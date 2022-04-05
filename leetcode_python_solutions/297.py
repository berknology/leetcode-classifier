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
