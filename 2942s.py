class Solution:
    def findWordsContaining(self, words, x):
        ans = []
        # indexing for loop
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] == x:
                    ans.append(i)
                    break
        sol = set(ans)
        return sol
        

y = Solution()
words = ["leet","code"]
x = "e"
y.findWordsContaining(words, x)
                    
        

        
