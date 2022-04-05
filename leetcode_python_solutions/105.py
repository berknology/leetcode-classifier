# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = preorder[::-1]
        return self.build_tree(preorder, inorder)
    
    def build_tree(self, preorder, inorder):
        if not inorder:
            return None
        val = preorder.pop()
        index = inorder.index(val)
        root = ListNode(val)
        root.left = self.build_tree(preorder, inorder[:index])
        root.right = self.build_tree(preorder, inorder[index+1:])
        return root
        
        
        
"""
preorder:   N L R
inorder:    L N R
postorder:  L R N
"""
