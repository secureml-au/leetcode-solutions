class Solution:
    def thirdMax(self, nums):
        first = second = third = float('-inf')
        for n in nums:
            if n == first or n == second or n == third:
                continue
            if n > first:
                first, second, third = n, first, second
            elif n > second:
                second, third = n, second
            elif n > third:
                third = n
        return third if third != float('-inf') else first