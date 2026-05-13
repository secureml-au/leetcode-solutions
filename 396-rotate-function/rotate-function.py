class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        f = sum(i * nums[i] for i in range(n))
        res = f
        for i in range(1, n):
            f = f + s - n * nums[n - i]
            res = max(res, f)
        return res