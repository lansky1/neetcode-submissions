class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        nextHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return nextHead
