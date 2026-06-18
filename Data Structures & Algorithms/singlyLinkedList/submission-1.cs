public class LinkedList {

    private Node head;
    private Node tail;
    private int count;

    public LinkedList() {
        this.head = null;
        this.tail = null;
        this.count = 0;
    }

    public int Get(int index) {
        if(index >= count) return -1;
        Node curr = new Node(0);
        curr = this.head;
        for(int i = 0; i < index; ++i) {
            curr = curr.next;
        }
        return curr.val;
    }

    public void InsertHead(int val) {
        Node newNode = new Node(val);
        newNode.next = this.head;
        this.head = newNode;
        if(head.next == null) this.tail = newNode;
        count++;
    }

    public void InsertTail(int val) {
        Node newNode = new Node(val);
        if (tail == null) {
            this.tail = newNode;
            this.head = newNode;
        }

        else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        count++;
    }

    public bool Remove(int index) {
        if(index >= count) return false;
        if(index == 0) {
            head = head.next;
            count--;
            return true;
        }

        Node curr = new Node(0);
        curr = this.head;
        for(int i = 1; i < index; ++i) {
            curr = curr.next;
        }
        if(curr.next == tail) tail = curr;
        curr.next = curr.next.next;
        count--;
        return true;
    }

    public List<int> GetValues() {
        Node curr = new Node(0);
        curr = this.head;
        List<int> values = new List<int>();
        for(int i = 0; i < count; ++i) {
            values.Add(curr.val);
            curr = curr.next;
        }
        return values;
    }
}

public class Node {
    public int val;
    public Node next;

    public Node(int val) {
        this.val = val;
        this.next = null;
    }
}