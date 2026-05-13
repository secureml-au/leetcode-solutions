class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1] * n
        idx = [0] * len(primes)
        vals = primes[:]

        for i in range(1, n):
            dp[i] = min(vals)
            for j in range(len(primes)):
                if dp[i] == vals[j]:
                    idx[j] += 1
                    vals[j] = dp[idx[j]] * primes[j]
        return dp[-1]