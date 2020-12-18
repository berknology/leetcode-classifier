# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        ans = [None]*k
        if not root:
            return ans
        length = self.find_len(root)
        div, mod = length//k, length%k
        pre = None
        for i in range(k):
            if not root:
                break
            ans[i] = root
            j = 0
            while root and j < div:
                pre = root
                root = root.next
                j += 1
            if root and mod > 0:
                pre = root
                root = root.next
                mod -= 1
            pre.next = None
        return ans
        
    def find_len(self, root):
        ans = 0
        while root:
            ans += 1
            root = root.next
        return ans
    
        
