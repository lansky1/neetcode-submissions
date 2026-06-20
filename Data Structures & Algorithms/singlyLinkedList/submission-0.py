'''
    TIME: 50:30 minutes
'''

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def get(self, index: int) -> int:
        new_node = self.head
        i = 0
        while new_node:
            if i == index:
                return new_node.val
            new_node = new_node.next
            i += 1
        return -1

    def insertHead(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = self.head

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.tail != None:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        new_node = ListNode(-1)
        new_node.next = self.head
        i = 0

        while new_node.next and i != index:
            new_node = new_node.next
            i += 1

        if new_node.next:
            if (new_node.next == self.head):
                self.head = self.head.next
            if (new_node.next == self.tail):
                self.tail = None if self.head is None else new_node
            new_node.next = new_node.next.next
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        new_node = self.head
        nodes = []
        while new_node:
            nodes.append(new_node.val)
            new_node = new_node.next
        return nodes


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
