class Solution:
    def findTheDifference(self, s, t):
        for c in t:
            if s.count(c) != t.count(c):
                return c