class Solution:
    def mincostTickets(self, days, costs):
        dp = [None] * len(days)
        def dfs(index):
            if (index >= len(days)):
                return 0
            if (dp[index] != None):
                return dp[index]

            dp[index] = float("inf")
            for day,cost in zip([1,7,30], costs):
                j = index
                while j < len(days) and days[j] < days[index] + day:
                    j += 1
                dp[index] = min(dp[index], cost + dfs(j))

            return dp[index]
        return dfs(0)
    

sol = Solution()
days = [1,4,6,7,8,20]
costs = [2,7,15]
print(sol.mincostTickets(days,costs))
            