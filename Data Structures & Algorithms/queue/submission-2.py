# ─────────────────────────────────────────────────────────
# Date : 28 Jun 2026
# ─────────────────────────────────────────────────────────
# Approach : Doubly Linked List using Double Sentinal Node
# Time : O(1) all operations
# Space: O(n)
# ─────────────────────────────────────────────────────────
# Notes : Claude suggested simplifying isEmpty and removing
#         dependencies from appendLeft and popLeft
# ─────────────────────────────────────────────────────────


class ListNode:
    def __init__(
        self, val: int = 0, prev: Optional["ListNode"] = None, next: Optional["ListNode"] = None
    ):
        self.val = val
        self.prev = prev
        self.next = next


class Deque:
    def __init__(self):
        self.count: int = 0
        self.head: ListNode = ListNode()
        self.tail: ListNode = ListNode(0, self.head)
        self.head.next = self.tail

    def isEmpty(self) -> bool:
        return self.count == 0

    def append(self, value: int) -> None:
        new_node: ListNode = ListNode(value, self.tail.prev, self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.count += 1

    def appendleft(self, value: int) -> None:
        new_node: ListNode = ListNode(value, self.head, self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.count += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        curr = self.tail.prev
        self.tail.prev = curr.prev
        curr.prev.next = self.tail
        self.count-=1
        return curr.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        curr = self.head.next
        self.head.next = curr.next
        curr.next.prev = self.head
        self.count-=1
        return curr.val
