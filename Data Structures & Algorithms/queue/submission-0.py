# ─────────────────────────────────────────────────────────
# Date : 26 Jun 2026
# ─────────────────────────────────────────────────────────
# Approach : Doubly Linked List
# Time : O(1) all operations
# ─────────────────────────────────────────────────────────
# Notes : Arrays would have been O(n) for Popleft
#         and AppendLeft.
#         Still not simple, want to simply the code.
# ─────────────────────────────────────────────────────────

class ListNode:
    def __init__(self, val: int = 0, prev: Optional['ListNode'] = None,
        next: Optional['ListNode'] = None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:

    def __init__(self):
        self.count: int = 0
        self.head: ListNode = ListNode()
        self.tail: ListNode = self.head

    def isEmpty(self) -> bool:
        return True if self.count == 0 else False

    def append(self, value: int) -> None:
        new_node: ListNode = ListNode(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.count+=1

    def appendleft(self, value: int) -> None:
        if self.isEmpty():
            self.append(value)
            return
        new_node: ListNode = ListNode(value)
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head
        self.count+=1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        x = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        self.count-=1
        return x

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        elif self.count == 1:
            return self.pop()
        x = self.head.next.val
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.count-=1
        if self.isEmpty():
            self.tail = self.head
        return x