# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = pre = ListNode()
        dummy.next = head
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
            head = head.next
        return dummy.next

