class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kmap = []
        curVal = nums[0]
        curFreq = 0
        nums = sorted(nums) #nlogn

        for i,v in enumerate(nums): #n
            if v == curVal:
                curFreq+=1
            else:
                kmap.append([curFreq,curVal])
                curFreq = 1
                curVal = v
        kmap.append([curFreq,curVal])

        kmap = sorted(kmap) #nlogn

        ans = [] 
        while len(ans) < k: #k
            ans.append(kmap.pop()[1])
            
        return(ans)