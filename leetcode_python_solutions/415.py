class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        num1 = list(num1)
        num2 = list(num2)
        carry = 0
        while num1 or num2 or carry:
            _sum = 0
            if num1:
                _sum += int(num1.pop())
            if num2:
                _sum += int(num2.pop())
            _sum += carry
            ans.append(str(_sum%10))
            carry = _sum//10
        return ''.join(ans[::-1])
