# ─────────────────────────────────────────────────────────
# Date : 28 Jun 2026
# ─────────────────────────────────────────────────────────
# Approach : One Queue
# Time : O(n) for Push, O(1) for Pop
# Space : O(n)
# ─────────────────────────────────────────────────────────
# Notes : will be expensive for push can reach O(n)
# ─────────────────────────────────────────────────────────

from collections import deque


class MyStack:
    def __init__(self):
        self.d = deque()

    def push(self, x: int) -> None:
        self.d.append(x)
        for i in range(1, len(self.d)):
            self.d.append(self.d.popleft())

    def pop(self) -> int:
        return self.d.popleft()

    def top(self) -> int:
        return self.d[0]

    def empty(self) -> bool:
        return len(self.d) == 0
