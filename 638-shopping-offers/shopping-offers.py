class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @cache
        def dfs(needs):
            # buy without offers
            cost = sum(needs[i] * price[i] for i in range(len(needs)))
            
            for offer in special:
                next_needs = []
                for i in range(len(needs)):
                    if offer[i] > needs[i]: # can't use this offer
                        break
                    next_needs.append(needs[i] - offer[i])
                else: # offer is valid
                    cost = min(cost, offer[-1] + dfs(tuple(next_needs)))
            return cost
        
        return dfs(tuple(needs))