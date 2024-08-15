class Solution:
    stringLengths = []
    # turn list into string
    def encode(self, strs): 
        ans = ""
        for word in strs:
            ans += word
            self.stringLengths.append(len(word))
        print(ans)
        return ans
    
    # turn string into a list
    def decode(self, s):
        curString = ""
        ans = []
        currentIndex = 0
        for i in range(len(s)):
            curString += s[i]
            if len(curString) == self.stringLengths[currentIndex]:
                ans.append(curString)
                curString = ""
                currentIndex += 1
        print(ans)
        return ans
        
        
sol = Solution()
s = ["we","say",":","yes"]
sol.decode(sol.encode(s))
