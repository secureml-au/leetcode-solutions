from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        
        p_count = Counter(p)
        s_count = Counter()
        res = []
        m = len(p)
        
        for i in range(len(s)):
            # add new char to window
            s_count[s[i]] += 1
            
            # remove char that's now outside window
            if i >= m:
                left_char = s[i - m]
                s_count[left_char] -= 1
                if s_count[left_char] == 0:
                    del s_count[left_char]
            
            # check if window matches
            if s_count == p_count:
                res.append(i - m + 1)
        
        return res