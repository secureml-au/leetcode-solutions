class Solution:
    def licenseKeyFormatting(self, s, k):
        # remove dashes and uppercase
        s = s.replace('-', '').upper()

        # build from right
        res = []
        count = 0

        for i in range(len(s) - 1, -1, -1):
            res.append(s[i])
            count += 1
            if count == k and i!= 0:
                res.append('-')
                count = 0

        return ''.join(reversed(res))