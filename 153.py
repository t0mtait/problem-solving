class Solution:
    def findMin(self, nums):
        if not nums:
            return -1

        p1 = 0
        p2 = len(nums)-1
        min = nums[p2]
        if nums[p1] < nums[p2]:
            min = nums[p1]
        
        if min == nums[p1]:
            loop = True
            index = p1+1
            while (loop):
                try:
                    if nums[index] < min:
                        min = nums[index]
                        index += 1
                    else:
                        loop = False
                except IndexError:
                    loop = False

        else:
            loop = True
            index = p2-1
            while (loop):
                try:
                    if nums[index] < min:
                        min = nums[index]
                        index -= 1
                    else:
                        loop = False
                except IndexError:
                    loop = False
        return min

sol = Solution()
nums = [3,4,5,6,1,2]
print(sol.findMin(nums))