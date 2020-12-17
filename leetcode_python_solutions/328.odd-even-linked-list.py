#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        odd_head = head.next
        even = head
        odd = head.next
        while odd and odd.next:
            even.next, even = odd.next, odd.next
            odd.next, odd = even.next, even.next
        even.next = odd_head
        return head

# @lc code=end

