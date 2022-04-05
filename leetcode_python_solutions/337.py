class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = {None: 0}
        return self._rob(root, memo)
    def _rob(self, root, memo):
        if root in memo:
            return memo[root]
        else:
            rob_now = 0
            rob_now += root.val
            if root.left:
                rob_now += self._rob(root.left.left, memo)
                rob_now += self._rob(root.left.right, memo)
            if root.right:
                rob_now += self._rob(root.right.left, memo)
                rob_now += self._rob(root.right.right, memo)
            memo[root] = max(rob_now, self._rob(root.left, memo)+self._rob(root.right, memo))
            return memo[root]
