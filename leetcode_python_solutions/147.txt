# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode()
        cur = head
        while cur:
            pre = dummy
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            nex = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = nex
        return dummy.next

    
"""
1-2-4

"""
