class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""
        
        need = {}
        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1
        
        left = 0
        count = 0
        min_len = float('inf')
        min_start = 0
        have = {}
        
        for right in range(len(s)):
            ch = s[right]
            if ch in have:
                have[ch] += 1
            else:
                have[ch] = 1
            
            if ch in need and have[ch] == need[ch]:
                count += 1
            
            while count == len(need):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                left_ch = s[left]
                have[left_ch] -= 1
                if left_ch in need and have[left_ch] < need[left_ch]:
                    count -= 1
                left += 1
        
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]