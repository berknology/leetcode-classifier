class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) !=  len(B): return False
        return B in A+A
