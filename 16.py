class Solution:

    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(target - current_sum) < abs(target - closest):
                    closest = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target  
        return closest


    def threeSum(self, nums):
        nums.sort()
        answer = []
        for i,n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            twoSums = self.twoSum(nums[i+1:], -n)
            for twoSum in twoSums:
                answer.append([n] + twoSum)
        return answer
    
    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        pairs = []
        while left < right:
            sum = nums[left] + nums[right]
            if sum < target or (left > 0 and nums[left] == nums[left - 1]):
                left += 1
            elif sum > target or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                right -= 1
            else:
                pairs.append([nums[left], nums[right]])
                left += 1
                right -= 1
        return pairs
        

nums = [-1,2,1,-4]
target = 1
x = Solution()
print(x.threeSumClosest(nums,target))