class Solution(object):
    def longestPalindrome(self, s):
        occmap = {}
        length = 0;
        extraChar = False;
        for char in s:
            if char in occmap:
                occmap[char]+= 1;
            else:
                occmap[char] = 1;
        for i in occmap:
            if occmap[i] == 1:
                extraChar = True;
            elif occmap[i]%2 == 0:
                length += occmap[i];
            else:
                extraChar = True;
                length += occmap[i]-1;
                
                
        if (extraChar):
            length = length + 1
        return length






        