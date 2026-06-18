class Deque {

    ListNode head;
    ListNode tail;
    int count;

    public Deque() {
        head = null;
        tail = null;
        count = 0;
    }

    public bool isEmpty() {
        return count == 0 ? true : false;
    }

    public void append(int value) {
        ListNode node = new ListNode(value);
        if(tail == null) {
            head = node;
            tail = node;
        }
        else {
            tail.next = node;
            node.prev = tail;
            tail = node;
        }
        count++;
    }

    public void appendleft(int value) {
        ListNode node = new ListNode(value);
        if(head == null) {
            head = node;
            tail = node;
        }
        else {
            node.next = head;
            head.prev = node;
            head = node;
        }
        count++;
    }

    public int pop() {
        if(count == 0) return -1;
        if(head == tail) {
            ListNode node = new ListNode(0);
            node = head;
            head = null;
            tail = null;
            count = 0;
            return node.value;
        }
        else {
            ListNode node = new ListNode(0);
            node = tail;
            tail = tail.prev;
            tail.next = null;
            count--;
            return node.value;
        }
    }

    public int popleft() {
        if(count == 0) return -1;
        if(head == tail) {
            ListNode node = new ListNode(0);
            node = head;
            head = null;
            tail = null;
            count = 0;
            return node.value;
        }
        else {
            ListNode node = new ListNode(0);
            node = head;
            head = head.next;
            head.prev = null;
            count--;
            return node.value;
        }
    }
}

public class ListNode {
    public int value;
    public ListNode prev;
    public ListNode next;

    public ListNode(int value) {
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}
