# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or (len(lists) == 1 and lists[0] is None):
            return 

        list1 = lists

        while(len(list1) != 1):
            list2 = []
            for i in range(0, len(list1), 2):
                if i+1 != len(list1):
                    new_head = self.merge2Lists(list1[i], list1[i+1])
                else:
                    new_head = list1[i]
                list2.append(new_head)
            list1 = list2

        return list1[0]

    def merge2Lists(self, list1, list2):
        curr = prev_node = ListNode(0)
        
        while list1 and list2:
            if list1.val <= list2.val:
                prev_node.next = list1
                list1 = list1.next

            else:
                prev_node.next = list2
                list2 = list2.next

            prev_node = prev_node.next

        if list2:
            prev_node.next = list2
        
        if list1:
            prev_node.next = list1

        return curr.next
