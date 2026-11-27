class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        p1 = 0
        p2 = len(s)-1

        while p2 > p1:
            if (s[p1] != s[p2]):
                if s[p1].isalnum() == False:
                    p1+=1
                elif s[p2].isalnum() == False:
                    p2-=1
                else:
                    print(s[p1] , s[p2])
                    return False
            else:
                p1+=1
                p2-=1
        return True
        
            
        