class ListNode:
    def __init__(self, url: int, prev: Optional['ListNode'] = None, 
                next: Optional['ListNode'] = None):
        self.val = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage: ListNode = ListNode(homepage)
        self.curr: ListNode = self.homepage

    def visit(self, url: str) -> None:
        new_node: ListNode = ListNode(url, self.curr, None)
        self.curr.next = new_node
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps-=1
        return self.curr.val


    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps-=1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)