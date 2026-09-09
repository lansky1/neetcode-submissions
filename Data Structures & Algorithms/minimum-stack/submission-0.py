# This wasn’t a difficult problem, but I’m guilty of reading the hint before I could arrive at the idea of maintaining the sub-list minimum.

class MinStack:
    def __init__(self):
        self.stack = []
        self.stepMinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stepMinStack:
            self.stepMinStack.append(min(val, self.stepMinStack[-1]))
        else:
            self.stepMinStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stepMinStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stepMinStack[-1]
