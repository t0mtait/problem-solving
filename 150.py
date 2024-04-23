class Solution:
    def evalRPN(self, tokens):
        nums = []
        for t in tokens:
            if (t != '+' and t != '-' and t != '*' and t != '/'):
                nums.append(t)
            else:
                if (t == '*'):
                    newNum = int(nums.pop()) * int(nums.pop())
                    nums.append(newNum)
                if (t == '/'):
                    num2 = nums.pop()
                    num1 = nums.pop()
                    newNum = int(int(num1) / int(num2))
                    nums.append(newNum)
                if (t == '+'):
                    newNum = int(nums.pop()) + int(nums.pop())
                    nums.append(newNum)
                if (t == '-'):
                    num2 = nums.pop()
                    num1 = nums.pop()
                    newNum = int(num1) - int(num2)
                    nums.append(newNum)
        return int(nums[0])
    

x = Solution()
tokens = ["4","3","-"]
print(x.evalRPN(tokens))
            

        