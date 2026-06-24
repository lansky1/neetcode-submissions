class ListNode {
   public:
    string val_;
    ListNode* prev = nullptr;
    ListNode* next = nullptr;

    ListNode(string val) { val_ = val; }

    ListNode(string val, ListNode* previousNode) {
        val_ = val;
        prev = previousNode;
    }
};

class BrowserHistory {
   public:
    ListNode* curr = nullptr;

    BrowserHistory(string homepage) {
        ListNode* home = new ListNode(homepage);
        curr = home;
    }

    void visit(string url) {
        ListNode* newNode = new ListNode(url, curr);
        curr->next = newNode;
        curr = curr->next;
    }

    string back(int steps) {
        while (curr->prev and steps--) {
            curr = curr->prev;
        }
        return curr->val_;
    }

    string forward(int steps) {
        while (curr->next and steps--) {
            curr = curr->next;
        }
        return curr->val_;
    }
};
