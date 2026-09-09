# Time 21:21

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
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

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val, self.head.next)
        self.head.next = newNode
        if self.head == self.tail:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        curr = self.head
        if curr.next is None:
            return False
        for i in range(index):
            if curr.next is None:
                return False
            curr = curr.next

        if curr.next is None:
            return False
        if curr.next == self.tail:
            self.tail = curr
        
        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        curr = self.head.next
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next

        return values
