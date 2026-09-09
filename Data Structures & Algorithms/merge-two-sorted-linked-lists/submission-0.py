# Time 08.30

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head

        while (list1 and list2):
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        if list1 is not None:
            curr.next = list1

        if list2 is not None:
            curr.next = list2

        return head.next
        