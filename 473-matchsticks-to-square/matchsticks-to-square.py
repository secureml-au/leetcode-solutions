class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4!= 0 or len(matchsticks) < 4:
            return False
        
        side = total // 4
        matchsticks.sort(reverse=True) # optimize: try big sticks first
        sides = [0] * 4
        
        def dfs(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if sides[j] + matchsticks[i] <= side:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
                if sides[j] == 0: # prune: if this empty side fails, others will too
                    break
            return False
        
        return dfs(0)