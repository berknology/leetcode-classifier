# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = p2 = head
        while n > 0:
            p1 = p1.next
            n -= 1
        if not p1:
            return head.next
        pre = None
        while p1:
            pre = p2
            p1 = p1.next
            p2 = p2.next
        pre.next = p2.next
        return head
        
        
"""
1 -> 2 -> 3 -> 4 -> 5 -> None
                         p1
               p2
         
1 -> None
      p1
p2

1 -> 2 -> None
          p1
     p2

"""
