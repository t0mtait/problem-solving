class Solution:
    def generateParenthesis(self, n):
        chars = []
        ans = []

        def makeChoice(open, close):
            if (open == n and open == close):
                ans.append("".join(chars))
                return 
                
            if (open < n):
                    chars.append('(')
                    makeChoice(open+1, close)
                    chars.pop()

            if (open > close):
                chars.append(')')
                makeChoice(open,close+1)
                chars.pop()
        makeChoice(0,0)
            
        return ans
    
            
            
                







x = Solution()
n = 3

print(x.generateParenthesis(n))
        