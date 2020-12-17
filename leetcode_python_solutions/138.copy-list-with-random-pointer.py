#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.hash_table = dict()
        return self.copy_list(head)

    def copy_list(self, head):
        if not head: return None
        if head in self.hash_table:
            return self.hash_table[head]
        cloned_node = Node(head.val)
        self.hash_table[head] = cloned_node
        cloned_node.next = self.copy_list(head.next)
        cloned_node.random = self.copy_list(head.random)
        return cloned_node

# @lc code=end

