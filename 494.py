class Solution:
    def findTargetSumWays(self, nums, target):
        sum = 0
        for i in nums:
            sum += i
        dp = [[None] * (2 * sum + 1) for _ in range(len(nums) + 1)]

        def backtrack(index, total):
            if (index >= len(nums)):
                if (total == target):
                    return 1
                return 0
            if (dp[index][total] != None):
                return dp[index][total]
            dp[index][total] = backtrack(index+1, total+nums[index]) + backtrack(index+1,total-nums[index])
            return dp[index][total]
        
        return backtrack(0, 0)




sol = Solution()
nums = [1,1,1,1,1]
target = 3
print(sol.findTargetSumWays(nums,target))

