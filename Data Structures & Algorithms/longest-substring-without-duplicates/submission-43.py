class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1] * 128
        left = 0
        best = 0

        for right, char in enumerate(s):
            code = ord(char)
            if last_seen[code] >= left:
                left = last_seen[code] + 1
            last_seen[code] = right
            if right - left + 1 > best:
                best = right - left + 1

        return best
