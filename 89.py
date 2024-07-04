class Solution(object):
    def grayCode(self, n):
        sol = []
        maxRange = (2 ** n) - 1
        for i in range (0,maxRange+1):
            sol.append(i ^ (i >> 1))
        return sol
        
s = Solution()
print(s.grayCode(2))
        