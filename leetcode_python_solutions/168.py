class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while n > 0:
            n = n-1
            digit = n%26
            ans.append(chr(ord('A') + digit))
            n = n//26
        return ''.join(ans[::-1])
