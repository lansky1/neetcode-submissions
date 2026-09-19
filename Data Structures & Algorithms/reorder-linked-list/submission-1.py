# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
            
        prev = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        list2 = self.reverse_list(slow) 
        list1 = head

        prev = ListNode(0)
        while list1 and list2:
            prev.next = list1
            prev = list1
            list1 = list1.next
            
            prev.next = list2
            prev = list2
            list2 = list2.next

    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
