class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) #nlogn
        ans = []

        for i in range(0,len(nums)-1): #N
            p1 = i+1
            p2 = len(nums)-1

            while p1 < p2: #LOGN
                sum = nums[i] + nums[p1] + nums[p2]
                if sum == 0:
                    if ([nums[i],nums[p1],nums[p2]] not in ans):
                        ans.append([nums[i],nums[p1],nums[p2]])
                    p1+=1
                    p2-=1
                elif sum > 0:
                    p2 -= 1
                elif sum < 0:
                    p1 += 1
        return ans
        
            
                        
        




    