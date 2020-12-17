#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        pre, mid = self.find_mid(head)
        root = TreeNode(mid.val)
        root.right = self.sortedListToBST(mid.next)
        if pre:
            pre.next = None
            root.left = self.sortedListToBST(head)
        else:
            root.left = None
        return root

    def find_mid(self, head):
        if not head: return None, None
        pre = None
        slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        return pre, slow

# @lc code=end

