class Solution:
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        
        neg = num < 0
        num = abs(num)
        res = []
        
        while num > 0:
            res.append(str(num % 7))
            num //= 7
        
        if neg:
            res.append('-')
        
        return ''.join(reversed(res))