# There is a better approach using two pointers - slow and fast. 
# Keep fast n steps ahead of slow, and then remove slow.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n == 1:
            return
        
        new_head = self.reverse_list(head)
        prev_node = ListNode(0)
        prev_node.next = new_head

        for _ in range(n-1):
            prev_node = prev_node.next

        if prev_node.next is new_head:
            new_head = new_head.next

        prev_node.next = prev_node.next.next

        new_head = self.reverse_list(new_head)
        return new_head

    def reverse_list(self, head):
        prev_node = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        return prev_node
