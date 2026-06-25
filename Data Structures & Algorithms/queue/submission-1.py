# ─────────────────────────────────────────────────────────
# Date : 26 Jun 2026
# ─────────────────────────────────────────────────────────
# Approach : Doubly Linked List
# Time : O(1) all operations
# Space: O(n)
# ─────────────────────────────────────────────────────────
# Notes : Claude suggested simplifying isEmpty and removing
#         dependencies from appendLeft and popLeft
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
        return self.count == 0

    def append(self, value: int) -> None:
        new_node: ListNode = ListNode(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.count+=1

    def appendleft(self, value: int) -> None:
        new_node: ListNode = ListNode(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next = new_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node
        self.count += 1

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
        x = self.head.next.val
        self.head.next = self.head.next.next
        if self.head.next:
            self.head.next.prev = self.head
        else:
            self.tail = self.head
        self.count -= 1
        return x