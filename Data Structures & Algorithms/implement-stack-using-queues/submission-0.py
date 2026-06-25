# ─────────────────────────────────────────────────────────
# Date : 26 Jun 2026
# ─────────────────────────────────────────────────────────
# Approach : Two Queues
# Time : O(n) for Push, O(1) for Pop
# Space : O(n) 
# ─────────────────────────────────────────────────────────
# Notes : will be expensive for push can reach O(n)
# ─────────────────────────────────────────────────────────

from collections import deque

class MyStack:

    def __init__(self):
        self.d1 = deque()
        self.d2 = deque()

    def push(self, x: int) -> None:
        if len(self.d1) == 0:
            self.d1.append(x)
        else:
            while len(self.d1) != 0:
                self.d2.append(self.d1.popleft())
            self.d1.append(x)
            while len(self.d2) != 0:
                self.d1.append(self.d2.popleft())

    def pop(self) -> int:
        return self.d1.popleft()

    def top(self) -> int:
        return self.d1[0]

    def empty(self) -> bool:
        return True if len(self.d1) == 0 else False
