class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        while left < right:
            mid = left + (right-left)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        if left == len(letters):
            return letters[0]
        else:
            return letters[left]
