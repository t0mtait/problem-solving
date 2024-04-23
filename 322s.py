class Solution(object):
    
    def coinChange(self, coins, amount):

        memo = { 0: 0}
    
        
        def subFunc(amount):
            if amount in memo:
                   return memo[amount]
                    
            if amount < 0:
                    return float('inf')
            
            minCoins = float('inf')
            for coin in coins:
                 numCoins = subFunc(amount-coin)
                 if numCoins != float('inf'):
                      minCoins = min(minCoins, numCoins + 1)
            
            memo[amount] = minCoins
            return minCoins
    
        minCoins = subFunc(amount)
        return minCoins if minCoins != float('inf') else -1

