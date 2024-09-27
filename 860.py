class Solution(object):
    def lemonadeChange(self, bills):
        c = 0
        ownedBills = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            ownedBills[bill]+=1

            if (bill == 10): # give back 5$
                if ownedBills[5] < 1:
                    return False
                ownedBills[5]-=1
                
            if (bill == 20): # give back 15$
                if ownedBills[10] > 0 and ownedBills[5] > 0:
                    ownedBills[10] -= 1
                    ownedBills[5] -= 1
                elif ownedBills[5] > 2:
                    ownedBills[5] -= 3
                else:
                    return False
        return True


bills = [5,5,10,10,20]
sol = Solution()
print(sol.lemonadeChange(bills))