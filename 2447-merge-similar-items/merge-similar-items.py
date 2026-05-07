class Solution:
    def mergeSimilarItems(self, items1, items2):
        weight = {}
        for v, w in items1 + items2:
            weight[v] = weight.get(v, 0) + w
        return sorted(weight.items())