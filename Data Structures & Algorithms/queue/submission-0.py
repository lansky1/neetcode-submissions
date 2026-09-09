class ListNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.nodeCount = 0
        self.head.next, self.tail.prev = self.tail, self.head 

    def isEmpty(self) -> bool:
        return True if self.nodeCount == 0 else False

    def append(self, value: int) -> None:
        newNode = ListNode(value, self.tail.prev, self.tail)
        self.tail.prev.next, self.tail.prev = newNode, newNode
        self.nodeCount+=1

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value, self.head, self.head.next)
        self.head.next.prev, self.head.next = newNode, newNode
        self.nodeCount+=1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        toBeDeletedNode = self.tail.prev
        newLeftNode = self.tail.prev.prev
        
        newLeftNode.next, self.tail.prev = self.tail, newLeftNode

        self.nodeCount-=1
        return toBeDeletedNode.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        toBeDeletedNode = self.head.next
        newRightNode = self.head.next.next
        newRightNode.prev, self.head.next = self.head, newRightNode

        self.nodeCount-=1
        return toBeDeletedNode.val
