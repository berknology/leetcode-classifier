# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(None)
        dummy.next = head
        while head and head.next:
            while head and head.next and head.val == head.next.val:
                head = head.next
            pre.next = head
            pre = head
            head = head.next
        return dummy.next

