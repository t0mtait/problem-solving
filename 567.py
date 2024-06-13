class Solution(object):
    def checkInclusion(self, s1, s2):
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        # create a hahsmap for s1 and s2 of all 0s for all 26 letters
        s1Letters = [0] * 26
        s2Letters = [0] * 26
        for i in range(len1):
            # update freq. value in hashmap for s1 and s2
            s1Letters[ord(s1[i]) - ord('a')] += 1
            s2Letters[ord(s2[i]) - ord('a')] += 1

        # check if s1 and s2 hashmaps matchup
        for i in range(len1, len2):
            if s1Letters == s2Letters:
                return True
            s2Letters[ord(s2[i]) - ord('a')] += 1
            s2Letters[ord(s2[i - len1]) - ord('a')] -= 1

        return s1Letters == s2Letters

sol = Solution()
s1 = "ab"
s2 = "eidboaoo"
print(sol.checkInclusion(s1, s2))