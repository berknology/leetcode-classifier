class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
        

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table = dict()
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.hash_table:
            return -1
        node = self.hash_table[key]
        self.delete(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_table:
            node = self.hash_table[key]
            node.val = value
            self.delete(node)
            self.add(node)
        else:
            node = ListNode(key, value)
            self.hash_table[key] = node
            self.add(node)
            if len(self.hash_table) > self.capacity:
                last_node = self.tail.pre
                del self.hash_table[last_node.key]
                self.delete(last_node)
    
    def add(self, node):
        next_node = self.head.next
        self.head.next = node
        node.next = next_node
        node.pre = self.head
        next_node.pre = node
        
    def delete(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



"""
h         t
[4,  2,   1]

hash_table

doubly linked list



"""
