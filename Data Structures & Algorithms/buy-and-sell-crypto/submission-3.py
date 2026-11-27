class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        buySell = [-1,-1]
        for i,v in enumerate(prices):
            for sellIndex in range(i,len(prices)):
                if prices[sellIndex] - v > bestProfit:
                    bestProfit = prices[sellIndex] - v
                    buySell = [i,sellIndex]
        return bestProfit
