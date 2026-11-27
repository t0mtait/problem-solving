class Solution:
    offset = 0;
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

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        midRow = int(len(matrix)/2)
        # target is too big for row
        while midRow < len(matrix)-1 and target > matrix[midRow][len(matrix[midRow])-1]:
            midRow = int( midRow + len(matrix) / 2 )

        # target is too small for row
        while midRow > 0 and len(matrix) > midRow and target < matrix[midRow][0]:
            midRow = int(midRow/2)
        if len(matrix) > midRow and self.search(matrix[midRow],target) > -1:
            return True
        return False