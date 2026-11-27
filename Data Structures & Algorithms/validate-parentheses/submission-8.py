class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0,len(s)):
            if s[i] in ['(','{','[']:
                stack.append(s[i])
            if len(stack) == 0:
                return False
            if s[i] == ')':
                if stack.pop() != '(':
                    return False
            if s[i] == ']':
                if stack.pop() != '[':
                    return False
            if s[i] == '}':
                if stack.pop() != '{':
                    return False
        if len(stack) == 0:
            return True
        return False