from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next: Optional[ListNode] = next


class MyLinkedList:

    def __init__(self):
        self.head: ListNode = ListNode()
        self.tail: ListNode = self.head

    def get(self, index: int) -> int:
        curr: Optional[ListNode] = self.head.next
        i: int = 0

        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        node: ListNode = ListNode(val, self.head.next)
        self.head.next = node
        if node.next is None:
            self.tail = node

    def addAtTail(self, val: int) -> None:
        node: ListNode = ListNode(val)
        self.tail.next = node
        self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        node: ListNode = ListNode(val)
        prev: ListNode = self.head
        i = 0
        while prev.next and i < index:
            prev = prev.next
            i += 1
        if i != index:
            return
        node.next = prev.next
        prev.next = node
        if prev is self.tail:
            self.tail = node

    def deleteAtIndex(self, index: int) -> None:
        prev: ListNode = self.head
        i = 0
        while prev.next and i != index:
            prev = prev.next
            i += 1
        if prev.next is None:
            return
        if prev.next is self.tail:
            self.tail = prev
        prev.next = prev.next.next