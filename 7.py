class Solution:
    def reverse(self, x):
        ans = 0
        isNeg = False
        stack = []
        for i in str(x):
            if (i == '-'):
                isNeg = True
            else:
                stack.append(int(i))
        print('stack:',stack)
        while len(stack) > 0:
            mult = 10**(len(stack)-1)
            ans += (stack.pop()*mult)
        if ((ans < (-2**31)) or (ans > ((2**31) -1))):
            return 0
        if (isNeg):
            return -ans
        return ans
        

sol = Solution()
x = 1234567899999
print(sol.reverse(x))
