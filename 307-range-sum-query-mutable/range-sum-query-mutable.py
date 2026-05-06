class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (self.n + 1)
        for i, x in enumerate(nums, 1):
            self._add(i, x)
    
    def _add(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i
    
    def _sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res
    
    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, diff)

    def sumRange(self, left, right):
        return self._sum(right + 1) - self._sum(left)