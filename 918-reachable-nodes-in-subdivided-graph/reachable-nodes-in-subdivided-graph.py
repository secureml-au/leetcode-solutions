from collections import defaultdict
import heapq

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = cnt
            graph[v][u] = cnt
        
        dist = {i: float('inf') for i in range(n)}
        dist[0] = 0
        heap = [(0, 0)]
        used = defaultdict(int)
        res = 0
        
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            res += 1
            for nei, cnt in graph[node].items():
                moves_left = maxMoves - d
                used[(node, nei)] = min(cnt, moves_left)
                nd = d + cnt + 1
                if nd < dist[nei] and nd <= maxMoves:
                    dist[nei] = nd
                    heapq.heappush(heap, (nd, nei))
        
        for u, v, cnt in edges:
            res += min(cnt, used[(u, v)] + used[(v, u)])
        return res