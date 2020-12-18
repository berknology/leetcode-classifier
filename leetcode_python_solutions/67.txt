class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        a_list = list(a)[::-1]
        b_list = list(b)[::-1]
        p_a, p_b = 0, 0
        carry = 0
        while p_a < len(a) or p_b < len(b) or carry > 0:
            _sum = 0
            if p_a < len(a):
                _sum += int(a_list[p_a])
                p_a += 1
            if p_b < len(b):
                _sum += int(b_list[p_b])
                p_b += 1
            _sum += carry
            ans.append(str(_sum%2))
            carry = _sum//2
        return ''.join(ans[::-1])
