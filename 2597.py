class Solution:
    def beautifulSubsets(self, nums, k):
        
        def loopIt(index, total):
                if index == len(nums):
                     return 1
                ans = loopIt(index+1, total)
                if not total[nums[index] + k] and not total[nums[index] - k]:
                     total[nums[index]]+=1
                     ans += loopIt(index+1, total)
                     total[nums[index]]-=1
                return ans

        return loopIt(0, defaultdict(int))-1
        

sol = Solution()
nums = [4, 2, 5, 9, 10, 3]
k = 1
print(sol.beautifulSubsets(nums, k))