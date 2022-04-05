class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = self.traverse(l1)
        stack2 = self.traverse(l2)
        carry = 0
        cur = ListNode(0)
        while stack1 or stack2 or carry:
            val = 0
            if stack1:
                val += stack1.pop()
            if stack2:
                val += stack2.pop()
            if carry:
                val += carry
            cur.val = val%10
            pre = ListNode(0)
            pre.next = cur
            cur = pre
            carry = val//10
        return pre.next
    def traverse(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack
