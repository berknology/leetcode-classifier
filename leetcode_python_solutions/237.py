# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pre = None
        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            pre = node
            node = node.next
        pre.next = None
