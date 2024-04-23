class Solution:
    def carFleet(self, target, position, speed):
        tsPair = sorted(zip(position,speed))
        timeTaken = []
        for pos,speed in tsPair[::-1]:
            print('car info: (S,P):',speed,',',pos)
            x = (target - pos) / speed
            timeTaken.append(x)
            if (len(timeTaken) > 1 and timeTaken[-1] <= timeTaken[-2]):
                timeTaken.pop()
        return len(timeTaken)


y = Solution()
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(y.carFleet(target,position, speed))


        