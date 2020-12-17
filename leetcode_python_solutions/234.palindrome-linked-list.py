#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        head2 = self.reverse_list(slow)
        
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
    
    def reverse_list(self, cur):
        pre, nex = None, None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

# @lc code=end

