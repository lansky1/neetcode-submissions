'''
    Comment: I have spend a day racking my brain for this solution. 
    It took me two days, and yet it was after seeing the old code in C#
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(-1)
        head = curr

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list2:
            curr.next = list2
        else:
            curr.next = list1
        
        return head.next
