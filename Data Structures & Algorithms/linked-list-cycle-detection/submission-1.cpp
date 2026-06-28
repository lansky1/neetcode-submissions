#include <unordered_set>

class Solution {
public:
    bool hasCycle(ListNode* head) {
        unordered_set<ListNode*> seen;
        ListNode* curr = head;

        while (curr!=nullptr) {
            if (seen.contains(curr)) return true;
            seen.insert(curr);
            curr = (*curr).next;
        }
        return false;
    }
};
