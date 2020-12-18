class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return '-'+self.convert(-num)
        elif num > 0:
            return self.convert(num)
        else:
            return '0'
            
    def convert(self, num):
        ans = []
        while num:
            ans.append(str(num%7))
            num = num//7
        return ''.join(ans[::-1])
