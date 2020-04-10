class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> None:
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return min(self.data)

minStack = MinStack()
minStack.push(3)
minStack.push(6)
minStack.push(-1)
minStack.push(-5)
# print(minStack.pop())
# print(minStack.top())
# print(minStack.getMin())
# print(minStack.pop())
# print(minStack.top())
# print(minStack.getMin())
