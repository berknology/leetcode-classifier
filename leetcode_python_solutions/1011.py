class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right-left)//2
            if not self.is_feasible(weights, mid, D):
                left = mid + 1
            else:
                right = mid
        return left
    def is_feasible(self, weights, mid, D):
        days = 1
        cur_weight = 0
        for weight in weights:
            cur_weight += weight
            if cur_weight > mid:
                days += 1
                cur_weight = weight
        return days <= D
