class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        res = 0
        
        for _ in range(maxMove):
            next_dp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if dp[i][j] > 0:
                        for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < m and 0 <= nj < n:
                                next_dp[ni][nj] = (next_dp[ni][nj] + dp[i][j]) % MOD
                            else:
                                res = (res + dp[i][j]) % MOD
            dp = next_dp
        return res