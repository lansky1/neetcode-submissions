import sys

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_idx_stack = []
        self.min_value = sys.maxsize

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_value:
            self.min_value = val
            self.min_idx_stack.append(len(self.stack)-1)

    def pop(self) -> None:
        if (len(self.stack)-1) == self.min_idx_stack[-1]:
            self.min_idx_stack.pop()
            self.min_value = self.stack[self.min_idx_stack[-1]] if len(self.min_idx_stack) > 0 else sys.maxsize
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value
