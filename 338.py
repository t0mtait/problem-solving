class Solution:
    def countBits(self, n):
        dp = [0] * (n + 1)
        iterator = 1
        for i in range (n+1):
            if i == 0 or i == 1:
                dp[i] = i
                # print(i, ': [',i,']')
            else:
                if 2**iterator == i:
                    dp[i] = 1
                    iterator += 1
                    # print(i,': [ 1 ]')
                else:
                    tmp = 2**(iterator-1)
                    dp[i] = dp[tmp]
                    dp[i] += dp[i-tmp]
                    # print(i,': [',tmp, 'with a remainder of', i - tmp,']')
                    # print(i,': [ ',dp[i],' ]')  
        return dp



# 0 0
# 1 1   # square 5. iterator = 3 tmp = 4
# 2 1
# 3 2
# 4 1
# 5 2
# 6 2
# 7 3
# 8 1
# 9 2
# 10 2
# 11 3
# 12 2
# 13 3

sol = Solution()
n = 16
print(sol.countBits(n))
        