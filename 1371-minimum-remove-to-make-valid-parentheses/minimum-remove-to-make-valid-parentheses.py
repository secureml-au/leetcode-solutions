class Solution:
    def minRemoveToMakeValid(self, s):
        s = list(s)
        stack = []
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        
        for i in stack:
            s[i] = ''
            
        return ''.join(s)