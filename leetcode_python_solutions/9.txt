class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        new_x = 0
        temp = x
        while temp:
            new_x = new_x*10+temp%10
            temp = temp//10
        return new_x == x
