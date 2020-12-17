#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.build_graph(root, None)
        queue = collections.deque([(target, 0)])
        visited = set([target])
        ans = []
        while queue:
            node, step = queue.popleft()
            if step == K:
                ans.append(node.val)
            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, step+1))
        return ans

    def build_graph(self, root, par):
        if not root: return
        neighbors = []
        if par: neighbors.append(par)
        if root.left: neighbors.append(root.left)
        if root.right: neighbors.append(root.right)
        root.neighbors = neighbors
        self.build_graph(root.left, root)
        self.build_graph(root.right, root)

# @lc code=end

