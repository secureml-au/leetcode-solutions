class Solution:
    def toHex(self, num):
        if num == 0:
            return "0"
        
        # handle negative with two's complement
        if num < 0:
            num += 2**32
        
        hex_chars = "0123456789abcdef"
        res = []
        
        while num > 0:
            digit = num & 15 # same as num % 16
            res.append(hex_chars[digit])
            num >>= 4 # same as num // 16
        
        return "".join(reversed(res))