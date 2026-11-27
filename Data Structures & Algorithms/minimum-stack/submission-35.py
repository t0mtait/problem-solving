class MinStack:

    def __init__(self):
        input = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
        self.vals = []
        self.min = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        queue = []
        if len(self.min) == 0 or self.min[len(self.min)-1] >= val:
            self.min.append(val)
        # print('PUSH selfmin' , self.min, 'VAL', self.vals)

    def pop(self) -> None:
        if self.vals.pop() == self.min[len(self.min)-1]:
            self.min.pop()
        # print('POP selfmin' , self.min, 'VAL', self.vals)
            

    def top(self) -> int:
        return self.vals[len(self.vals)-1]

    def getMin(self) -> int:  # always called on non-empty stack,  O(1) time
        return self.min[len(self.min)-1]
