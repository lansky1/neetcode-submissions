# Time 9.54
# This can be done using doubly linked list, with two placeholder nodes.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head
        if curr.next is None:
            return -1
        for i in range(index):
            if curr.next is None:
                return -1
            curr = curr.next

        return -1 if curr.next is None else curr.next.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, self.head.next)
        self.head.next = newNode
        if self.head == self.tail:
            self.tail = newNode

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        newNode = ListNode(val)
        for i in range(index):
            if curr.next is None:
                return
            curr = curr.next

        if curr.next is None:
            self.tail = newNode

        newNode.next = curr.next
        curr.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        if curr.next is None:
            return
        for i in range(index):
            if curr.next is None:
                return
            curr = curr.next

        if curr.next is None:
            return
        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next
