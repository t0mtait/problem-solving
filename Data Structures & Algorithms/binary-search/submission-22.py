

class Solution:
    offset = 0 
    def search(self, nums: List[int], target: int) -> int:
        print(nums)
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return self.offset
            return -1
       
        else:
            mid = int(len(nums)/2)
            if nums[mid] == target:
                return mid + self.offset
            elif target > nums[mid]:
                self.offset += mid
                return self.search(nums[mid:len(nums)],target)
            elif target < nums[mid]:
                return self.search(nums[0:mid],target)
            return -1