from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        heap = [(0, src, k + 1)]
        visited = {}
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > 0:
                if node not in visited or visited[node] < stops:
                    visited[node] = stops
                    for nei, price in graph[node]:
                        heapq.heappush(heap, (cost + price, nei, stops - 1))
        return -1