class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        min_count = n
        res = 0
        for i in range(n):
            count = sum(dist[i][j] <= distanceThreshold for j in range(n) if i!= j)
            if count <= min_count:
                min_count = count
                res = i
        return res