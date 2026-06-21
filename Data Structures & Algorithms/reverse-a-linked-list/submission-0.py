'''
    Comment: Have to maintain two nodes and an extra condition
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head
        next_node: Optional[ListNode] = head.next

        while curr.next:
            curr.next = prev
            prev = curr
            curr = next_node
            next_node = next_node.next

        curr.next = prev

        return curr