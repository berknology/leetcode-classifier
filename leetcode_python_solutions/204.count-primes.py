#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True]*n
        is_prime[0:2] = [False, False]
        for i in range(2, n):
            for j in range(i*i, n, i):
                is_prime[j] = False
        return sum(is_prime)


# [0,     1,      2,    3,   4,    5,     6,    7,     8,     9  ]
# [False, False, True, True, False, True, False, True, False, False]

# @lc code=end

