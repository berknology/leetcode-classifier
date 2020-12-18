class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m*n != r*c: return nums
        cnt = 0
        ans = [[0]*c for _ in range(r)]
        for i in range(m):
            for j in range(n):
                row = cnt//c
                col = cnt%c
                cnt += 1
                ans[row][col] = nums[i][j]
        return ans
        
