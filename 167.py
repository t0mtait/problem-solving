class Solution:
    def twoSum(self, numbers,target):
        leftSlider = 0
        rightSlider = len(numbers)-1
        sum = numbers[leftSlider] + numbers[rightSlider]
        while (sum != target):
            if (sum < target):
                if (leftSlider == len(numbers)-1):
                    return -1
                else:
                    leftSlider+=1
                    sum = numbers[leftSlider] + numbers[rightSlider]

            else:
                if (rightSlider == 0):
                    return -1
                else:
                    rightSlider-=1
                    sum = numbers[leftSlider] + numbers[rightSlider]
        ans = []
        ans.append(leftSlider+1)
        ans.append(rightSlider+1)
        return ans




x = Solution()
numbers = [2,7,11,15]
target = 9

print(x.twoSum(numbers,target))