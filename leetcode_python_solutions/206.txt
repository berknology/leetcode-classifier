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
