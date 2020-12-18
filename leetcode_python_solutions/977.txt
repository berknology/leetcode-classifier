class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = []
        left, right = 0, len(A)-1
        while left <= right:
            if abs(A[left]) >= abs(A[right]):
                ans.append(A[left]**2)
                left += 1
            else:
                ans.append(A[right]**2)
                right -= 1
        return ans[::-1]
        
