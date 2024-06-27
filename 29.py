class Solution(object):
    def divide(self, dividend, divisor):
        # overflow
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        negative = (dividend < 0) != (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        ans = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                ans += i
                i <<= 1
                temp <<= 1
        
        return -ans if negative else ans

sol = Solution()
print(sol.divide(-2147483648, -1))