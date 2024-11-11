class Solution:
    def longestCommonSubsequence(self, text1, text2):
        table = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    
        for i in range(0, len(text1)):
            for j in range(0,len(text2)):
                if text1[i] == text2[j]:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    if i == 0 and j == 0:
                        table[i][j] = 0
                    if i == 0:
                        table[i][j] = table[i][j-1]
                    elif j == 0:
                        table[i][j] = table[i-1][j]
                    table[i][j] = max(table[i-1][j], table[i][j-1])


        # print the table
        # arr = []
        # for i in text2:
        #     arr.append(i)
        # print(arr)
        # print()
        # for i in range(len(text1)):
        #     print(text1[i] , table[i])

        return table[len(text1)-1][len(text2)-1]
        
        
    
    


text1 = "oxcpqrsvwf"
text2 = "shmtulqrypy"
print(Solution.longestCommonSubsequence(text1, text2)) # 3
        
        