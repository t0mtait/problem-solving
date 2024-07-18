class Solution(object):
    def subsets(self, nums):
        ans = []
        
        def backtracking(i):
            # skip
            if i == len(nums):
                return ans
            