class Solution:
    def scoreOfString(self, s):
        score = 0
        prevScore = ord(s[0])
        for index,value in enumerate(s):
            if (index > 0):
                score += abs(ord(value)-prevScore)
                prevScore = abs(ord(value))
            if (index == len(s)-1):
                return score
            

    



sol = Solution()
s = 'hello'
print(sol.scoreOfString(s))
        