class Solution:
    def toHex(self, num: int) -> str:
        self.hash_map = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        if num == 0:
            return '0'
        elif num > 0:
            return self.convert(num)
        else:
            return self.convert(2**32+num)
    def convert(self, num):
        ans = []
        while num:
            digit = num%16
            if digit < 10:
                ans.append(str(digit))
            else:
                ans.append(self.hash_map[digit])
            num = num//16
        return ''.join(ans[::-1])
