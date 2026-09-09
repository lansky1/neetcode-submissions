class ListNode:
    def __init__(self, url, prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homePage = ListNode(homepage)
        self.openPage = self.homePage

    def visit(self, url: str) -> None:
        newWebsite = ListNode(url)
        self.openPage.next, newWebsite.prev = newWebsite, self.openPage
        self.openPage = newWebsite

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.openPage.prev is None:
                break
            self.openPage = self.openPage.prev

        return self.openPage.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.openPage.next is None:
                break
            self.openPage = self.openPage.next

        return self.openPage.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)