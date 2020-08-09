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


"""
Time complexity: O(n)
Space complexity: O(n)
"""
