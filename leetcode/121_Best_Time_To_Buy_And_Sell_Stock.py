class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        smallestSoFar = prices[0]
        profitMargin = 0
        
        for i in range(1, len(prices)):
            if prices[i] < smallestSoFar:
                smallestSoFar = prices[i]
            else:
                profitMargin = max(profitMargin, prices[i] - smallestSoFar)
        
        return profitMargin
