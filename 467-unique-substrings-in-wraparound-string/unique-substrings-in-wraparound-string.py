class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        count = [0] * 26
        max_len = 0
        
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i-1])) % 26 == 1:
                max_len += 1
            else:
                max_len = 1
            idx = ord(s[i]) - ord('a')
            count[idx] = max(count[idx], max_len)
        
        return sum(count)