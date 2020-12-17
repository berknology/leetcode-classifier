#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if not root: return [None]*k
        ans = [None]*k
        length = self.find_length(root)
        div = length//k
        mod = length%k
        for i in range(k):
            ans[i] = root
            times = div + (mod > 0) - 1
            while root and times > 0:
                root = root.next
                times -= 1
            mod -= 1
            if not root: break
            root.next, root = None, root.next
        return ans

    def find_length(self, root):
        length = 0
        while root:
            length += 1
            root = root.next
        return length

# @lc code=end

