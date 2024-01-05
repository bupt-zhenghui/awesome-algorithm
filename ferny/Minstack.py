class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: self.stack.append((val,val))
        else:
            (a, min_val) = self.stack[-1]
            if val <= min_val:
                self.stack.append((val, val))
            else:
                self.stack.append((val, min_val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        else:
            return

    def top(self) -> int:
        a, b = self.stack[-1]
        return a

    def getMin(self) -> int:
        a, b = self.stack[-1]
        return b

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
