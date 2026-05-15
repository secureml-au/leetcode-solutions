class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(pos, used):
            if pos > n:
                return 1
            count = 0
            for num in range(1, n + 1):
                if not used & (1 << num) and (num % pos == 0 or pos % num == 0):
                    count += dfs(pos + 1, used | (1 << num))
            return count
        
        return dfs(1, 0)