class MinStack(object):

    def __init__(self):
        self.arr = []
        self.point = 0

    def push(self, val):
        self.arr.append(val)
        self.point += 1

    def pop(self):
        self.arr.pop()

    def top(self):
        return self.arr[-1]

    def getMin(self):
        min = self.arr[0]
        for elem in self.arr:
            if elem < min:
                min = elem
        return min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()