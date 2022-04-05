# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(None)
        dummy.next = head
        cur_val = None
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = head
                head = head.next
        return dummy.next

        
"""
         1->  1  -> 1  -> 2   -> 3
dummy                  -> 
                       pre
                       head 

"""
