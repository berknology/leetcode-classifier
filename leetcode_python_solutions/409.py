class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = collections.Counter(s)
        ans = 0
        n_odd = 0
        for key in cnt:
            if cnt[key]%2 == 0:
                ans += cnt[key]
            else:
                ans += (cnt[key]//2)*2
                n_odd += 1

        return ans + 1 if n_odd > 0 else ans


