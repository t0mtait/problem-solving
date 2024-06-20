class Solution:
    def maxProfit(self, prices):
        profit = 0
        for index,value in enumerate(prices):
            if (index < len(prices)-1):
                if (prices[index+1] > value):
                    profit = profit + prices[index+1] - value
            else:
                return profit
            


sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))