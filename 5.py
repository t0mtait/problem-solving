class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.helper(s, i, i)
            len2 = self.helper(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
            
        return s[start:end + 1]
            
    def helper(self, s, left, right):
        if s is None or left > right:
            return 0
    
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1

sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))