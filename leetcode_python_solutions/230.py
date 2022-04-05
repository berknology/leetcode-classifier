class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            node = stack.pop()
            k -= 1
            if k == 0: return node.val
            current = node.right
