class Solution:
    def longestConsecutive(self, nums):
        numset = set(nums)
        highestCount = 0

        for n in nums:
            if not(n-1 in numset):
                count = 0
                while (n + count) in numset:
                    count+=1
                highestCount = max(count,highestCount)
        return highestCount


            
    



sol = Solution()
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))


