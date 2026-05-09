class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.history.append(homepage)
        self.current = 0

    def visit(self, url: str) -> None:
        self.current += 1
        self.history[self.current:] = [url]

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

