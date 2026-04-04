class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
       
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.tail.prev = self.head
        self.head.next = self.tail

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node):
        head_next = self.head.next
        self.head.next = node
        head_next.prev = node
        node.prev = self.head
        node.next = head_next
    
    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def pop_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            
            node = Node(key, value)
            self.add_to_head(node)
            self.cache[key] = node

            if len(self.cache) > self.capacity:
                lru = self.pop_tail()
                del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)