# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        while curr.next is not None:
            next_node = curr.next
            node = curr
            while node.next.next is not None:
                node = node.next
            last_node = node.next
            node.next = None
            curr.next = last_node
            last_node.next = None if last_node == next_node else next_node
            curr = next_node