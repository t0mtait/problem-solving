class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        smallnums = nums[:len(nums)//2]
        largenums = nums[len(nums)//2:]
        nums = []
        for i in range(len(smallnums)):
            nums.append(smallnums[i])
            if i < len(largenums):
                nums.append(largenums[i])
        if len(largenums) > len(smallnums):
            nums.append(largenums[-1])
        print('nums:' , nums)
        return nums

sol = Solution()
nums = [1,5,1,1,6,4]
print(sol.wiggleSort(nums))