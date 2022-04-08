class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        ans = 0
        MOD = 10**9 + 7
        for i in range(len(arr)):
            new_sum = target - arr[i]
            left, right = i+1, len(arr)-1
            while left < right:
                if arr[left] + arr[right] < new_sum:
                    left += 1
                elif arr[left] + arr[right] > new_sum:
                    right -= 1
                else:
                    if arr[left] == arr[right]:
                        ans += (right-left+1)*(right-left)//2
                        ans %= MOD
                        break
                    else:
                        n_left = n_right = 1
                        while left < right and arr[left] == arr[left+1]:
                            left += 1
                            n_left += 1
                        while left < right and arr[right] == arr[right-1]:
                            right -= 1
                            n_right += 1
                        ans += n_left*n_right
                        ans %= MOD
                        left += 1
                        right -=1
        return ans
