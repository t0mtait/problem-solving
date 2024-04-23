
class Solution:
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                ans[stackIndex] = (i - stackIndex)
            stack.append([t,i])
        return ans
        


x = Solution()
temperatures = [73,74,75,71,69,72,76,73]