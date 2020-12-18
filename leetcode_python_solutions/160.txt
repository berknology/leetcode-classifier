class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = self.find_length(headA)
        len_b = self.find_length(headB)
        while len_a > len_b:
            headA = headA.next
            len_a -= 1
        while len_a < len_b:
            headB = headB.next
            len_b -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    
    def find_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
