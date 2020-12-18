# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(slow)
        new_head = self.merge(h1, h2)
        return new_head
    
    def merge(self, h1, h2):
        dummy = cur = ListNode()
        while h1 and h2:
            if h1.val <= h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        cur.next = h1 or h2
        return dummy.next
    
    
"""
dummy
cur   

                1   ->    3
                
                
                2   ->    4


"""
