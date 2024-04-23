class Solution:
    def getConcatenation(self, nums):
         ans = nums.copy()
         for i in nums:
            ans.append(i)
         return ans
    
    
x = Solution()
nums = [1,2,1]
x.getConcatenation(nums)
