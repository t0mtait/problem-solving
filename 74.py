class Solution:
    def searchMatrix(self, matrix, target):
        nrows = len(matrix)
        ncols = len(matrix[0])
    
        minVal = matrix[0][0]
        maxVal = matrix[nrows-1][ncols-1]

        # if target is smaller than smallest element or larger than largest element
        if (target < minVal) or (target > maxVal):
            return False


        # implement a binary-search approach
        def bs(matrix, left, right, up, down):
            if left > right or up > down:
                return False
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            midcol = left + (right - left) // 2

            row = up
            while row <= down and matrix[row][midcol] <= target:
                if matrix[row][midcol] == target:
                    return True
                row += 1

            return bs(matrix, left, midcol - 1, row, down) or bs(matrix, midcol + 1, right, up, row - 1)

        return bs(matrix, 0, ncols - 1, 0, nrows - 1)





sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(sol.searchMatrix(matrix,target))

