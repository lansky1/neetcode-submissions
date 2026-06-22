// list1->val is shorthand for (*list1).val

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode(-1);
        ListNode* head = dummy;

        while (list1!=nullptr && list2!=nullptr) {
            if (list1->val <= list2->val) {
                dummy->next = list1;
                list1 = list1->next;
            }
            else {
                dummy->next = list2;
                list2 = list2->next;
            }
            dummy = dummy->next;
        }

        if (list1 == nullptr) {
            dummy->next = list2;
        }
        else {
            dummy->next = list1;
        }

        return head->next;
    }
};