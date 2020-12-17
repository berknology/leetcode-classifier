#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return
        p1 = p2 = head
        while n > 0:
            p2 = p2.next
            n -= 1
        if not p2: return head.next
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        p1.next = p1.next.next
        return head
        
# @lc code=end

