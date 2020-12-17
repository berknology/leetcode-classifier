#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: 
            return None
        head = cur = ListNode(0)
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
        while min_heap:
            _, index = heapq.heappop(min_heap)
            node = lists[index]
            cur.next = node
            if node.next:
                node = node.next
                heapq.heappush(min_heap, (node.val, index))
                lists[index] = node
            cur = cur.next
        return head.next

# @lc code=end

