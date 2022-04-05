class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][-1])))
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][-1]
