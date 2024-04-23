class Solution:
    def maxArea(self, height):
        leftSlider = 0
        rightSlider = len(height)-1
        area = 0
        maxArea = 0
        loop = True
        while (loop):
            area = (rightSlider - leftSlider)*min(height[leftSlider],height[rightSlider])
            if (area > maxArea):
                print('new maxarea found: ', height[leftSlider], height[rightSlider])
                maxArea = area
            else:
                if (height[leftSlider] >= height[rightSlider]):
                    if (rightSlider-1 == leftSlider):
                        loop = False
                    else:
                        rightSlider-=1
                else:
                    if (leftSlider+1 == rightSlider):
                        loop = False
                    leftSlider+=1
        return maxArea

    




s = Solution()
height = [1,1]
print(s.maxArea(height))