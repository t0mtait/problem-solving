class Solution(object):
    def canPartition(self, nums):
        memo = {}
        def dfs(sum,target, index):
            if (sum,index) in memo:
                return memo[(sum,index)]
            if index == len(nums):
                return False
            if sum == target:
                return True
            if sum > target:
                return False
            else:
                memo[(sum, index)] = dfs(sum + nums[index], target, index + 1) or dfs(sum, target, index + 1)
                return dfs(sum+nums[index],target,index+1) or dfs(sum,target,index+1)
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        return dfs(0,target,0)
            

        
                
            

            

            

        
        
        


nums = [1,2,3,4,5,6,7]
sol = Solution()
print(sol.canPartition(nums))
        