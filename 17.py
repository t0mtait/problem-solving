class Solution(object):
    def letterCombinations(self, digits):
        digitMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"qprs",
            "8":"tuv",
            "9":"wxyz"
        }
        ans = []
        def subFunc(i, curr):
            if len(curr) == len(digits):
                ans.append(curr)
                return ans
            for j in digitMap[digits[i]]:
                subFunc(i+1,curr + j)
        
        if len(digits) > 0:
            subFunc(0, "")

        return ans
        

