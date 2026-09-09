# Time 05.30

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        curr = head

        # What about empty list?
        # Single element list
        # multi element list

        while curr:
            nextNode = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = nextNode
        
        return prevNode