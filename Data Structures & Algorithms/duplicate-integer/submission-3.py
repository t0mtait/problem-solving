class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i,v in enumerate(nums):
            if i > 0 and nums[i-1] == v:
                return True
            if len(nums) > i + 1 and nums[i+1] == v:
                return True
        return False
