#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if not head: return head
        # pre, cur = None, head
        # while cur:
        #     nex = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = nex
        # return pre
        if not head or not head.next: return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

# @lc code=end

