class Solution:
    def findDuplicate(self,nums):
        hashmap = {}
        for num in nums:
            if (num in hashmap):
                return num
            else:
                hashmap[num] = 1

sol = Solution()
nums = [1,3,4,2,2]
print(sol.findDuplicate(nums))