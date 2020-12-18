class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True]*n
        is_prime[0:2] = [False, False]
        for i in range(2, n):
            for j in range(i*i, n, i):
                is_prime[j] = False
        return sum(is_prime)
