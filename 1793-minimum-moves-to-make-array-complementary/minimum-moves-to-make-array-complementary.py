class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        diff = [0] * (2 * limit + 2) # range 2 to 2*limit

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            if a > b: a, b = b, a # a <= b

            # For target T in [2, 2*limit]:
            # 2 moves: baseline, for all T
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # 1 move range: [a+1, b+limit], subtract 1 move there
            diff[a + 1] -= 1
            diff[b + limit + 1] += 1

            # 0 move: [a+b, a+b], subtract another 1 move
            diff[a + b] -= 1
            diff[a + b + 1] += 1

        res = n # max is n pairs * 2 moves
        curr = 0
        for i in range(2, 2 * limit + 1):
            curr += diff[i]
            res = min(res, curr)

        return res