from collections import defaultdict

class Solution:
    def minEdgeReversals(self, n, edges):
        g = defaultdict(list)
        for u, v in edges:
            g[u].append((v, 0)) # u->v is original, cost 0
            g[v].append((u, 1)) # v->u is reversed, cost 1
        
        res = [0] * n
        
        def dfs1(u, p):
            for v, cost in g[u]:
                if v == p: continue
                res[0] += cost
                dfs1(v, u)
        
        def dfs2(u, p):
            for v, cost in g[u]:
                if v == p: continue
                # when moving root u->v: 
                # res[v] = res[u] - cost + (1 - cost)
                # because if cost=0, we gain +1. if cost=1, we save -1
                res[v] = res[u] - cost + (1 - cost)
                dfs2(v, u)
        
        dfs1(0, -1)
        dfs2(0, -1)
        return res