'''
    Comment: I have spend a day racking my brain for this solution
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head: Optional[ListNode] = ListNode(-1)
        curr: Optional[ListNode] = ListNode(-1)
        head = curr

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next

        if list1 is None and list2 is not None:
            curr.next = list2
        elif list2 is None and list1 is not None:
            curr.next = list1
        else:
            pass
        
        return head.next


        

    

