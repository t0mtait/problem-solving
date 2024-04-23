# CREATE A FUNCTION 


# WHEN GIVEN AN AMOUNT IN DOLLARS RETURN THE AMOUNT OF PENNIES, NICKELS, DIMES, AND QUARTERS THAT MAKE UP THAT AMOUNT



class Solution:
    def formula(self, amount):
        penny = 0.01
        nickel = 0.05
        dime = 0.10
        quarter = 0.25

        a_penny = amount / penny
        a_nickel = amount / nickel
        a_dime = amount / dime
        a_quarter = amount / quarter

        print ('quarters' , a_quarter , ' dimes: ' , a_dime , 'nickels' , a_nickel, 'pickles' , a_penny)



x = Solution() 
amount = 130
x.formula(amount)