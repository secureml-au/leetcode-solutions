class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        idx = list(range(len(positions)))
        idx.sort(key=lambda i: positions[i])
        stack = [] # stores [health, original_index]
        
        for i in idx:
            if directions[i] == 'R':
                stack.append([healths[i], i])
            else:
                while stack and directions[stack[-1][1]] == 'R':
                    rh, ri = stack[-1]
                    if rh > healths[i]:
                        stack[-1][0] -= 1
                        healths[i] = 0
                        break
                    elif rh < healths[i]:
                        stack.pop()
                        healths[i] -= 1
                    else:
                        stack.pop()
                        healths[i] = 0
                        break
                if healths[i] > 0:
                    stack.append([healths[i], i])
        
        res = []
        for h, i in sorted(stack, key=lambda x: x[1]):
            res.append(h)
        return res