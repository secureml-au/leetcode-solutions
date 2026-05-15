class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = []
        
        for i in range(n):
            dp[i][i] = True
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = s[i] == s[j] and (l == 2 or dp[i+1][j-1])
        
        def dfs(start, path):
            if start == n:
                res.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    dfs(end + 1, path + [s[start:end+1]])
        
        dfs(0, [])
        return res