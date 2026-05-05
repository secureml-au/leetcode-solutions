from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        heap = [(0, k)]
        
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for nei, w in graph[node]:
                if d + w < dist[nei]:
                    dist[nei] = d + w
                    heapq.heappush(heap, (dist[nei], nei))
        
        max_dist = max(dist.values())
        return max_dist if max_dist < float('inf') else -1