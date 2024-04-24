class Solution(object):
    index = 0
    def search(self, nums, target):
        if (len(nums) == 1):
            if (nums[0] == target):
                return self.index
            if (nums[0] != target):
                return -1
        else:
            middle = (len(nums) // 2)
            if (nums[middle] > target):
                nums = nums[:middle]
            else:
                self.index += middle
                nums = nums[middle:]
            print(nums)
            return self.search(nums,target)

    


x = Solution()
nums = [-1,0,3,5,9,12]
target = 9

print(x.search(nums,target))