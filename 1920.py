class Solution:
    def buildArray(self, nums):
        newNums = []
        for i in range(0,len(nums)):
            newNums.append(nums[nums[i]]) 
        return newNums

sol = Solution()
nums = [0,2,1,5,3,4]

print(sol.buildArray(nums))