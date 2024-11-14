class Solution:
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        if s[len(s)-1] == t[len(t)-1]:
            s = s[:-1]
            t = t[:-1]
        else:
            t = t[:-1]
        return self.isSubsequence(s,t)

        

sol = Solution()
s = "abc"
t = "ahbgdc"
print(sol.isSubsequence(s,t))
