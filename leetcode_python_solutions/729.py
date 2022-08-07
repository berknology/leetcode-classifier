class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar:

    def __init__(self):
        self.root = None

    def insert(self, root, node) -> True:
        if not root:
            root = node
            return root, True
        if root.start >= node.end:
            root.left, flag = self.insert(root.left, node)
            return root, flag
        elif root.end <= node.start:
            root.right, flag = self.insert(root.right, node)
            return root, flag
        else:
            return root, False

    def book(self, start: int, end: int) -> bool:
        self.root, flag = self.insert(self.root, TreeNode(start, end))
        return flag

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
