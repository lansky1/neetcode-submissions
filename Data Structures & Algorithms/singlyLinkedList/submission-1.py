'''
    Comment: Took Help from Claude on How to improve
'''

from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next: Optional[ListNode] = next


class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = ListNode()
        self.tail: Optional[ListNode] = self.head

    def get(self, index: int) -> int:
        curr: Optional[ListNode] = self.head.next
        i: int = 0

        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        node: ListNode = ListNode(val, self.head.next)
        self.head.next = node
        if node.next is None:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node: ListNode = ListNode(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        prev: ListNode = self.head
        i = 0
        while prev.next and i!=index:
            prev = prev.next
            i += 1
        if prev.next is None:
            return False
        if prev.next is self.tail:
            self.tail = prev
        prev.next = prev.next.next
        return True

    def getValues(self) -> List[int]:
        curr: Optional[ListNode] = self.head.next
        nodes: List[int] = []

        while curr:
            nodes.append(curr.val)
            curr = curr.next

        return nodes
