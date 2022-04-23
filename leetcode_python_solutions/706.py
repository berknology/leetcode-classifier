class LinkedNode:
    def __init__(self, key, val, nex):
        self.key = key
        self.val = val
        self.next = nex


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def get_b_index(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        b_index = self.get_b_index(key)
        node = self.buckets[b_index]
        while node:
            if node.key == key:
                node.val = value
                return
            node = node.next
        new_node = LinkedNode(key, value, self.buckets[b_index])
        self.buckets[b_index] = new_node

    def get(self, key: int) -> int:
        b_index = self.get_b_index(key)
        node = self.buckets[b_index]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        b_index = self.get_b_index(key)
        node = self.buckets[b_index]
        if not node:
            return
        if node.key == key:
            self.buckets[b_index] = node.next
            return
        pre, node = node, node.next
        while node:
            if node.key == key:
                pre.next = node.next
                return
            pre, node = node, node.next
