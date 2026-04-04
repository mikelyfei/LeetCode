from collections import defaultdict

class LFUCache:
    class Node:
        def __init__(self, key=0, value=0, freq=1):
            self.key = key
            self.value = value
            self.freq = freq
            self.prev = None
            self.next = None
    
    class DoublyLinkedList:
        def __init__(self):
            self.head = LFUCache.Node()
            self.tail = LFUCache.Node()
            self.tail.prev = self.head
            self.head.next = self.tail
            self.size = 0

        def add_to_head(self, node):
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            self.size += 1

        def remove_node(self, node):
            node.next.prev = node.prev
            node.prev.next = node.next
            self.size -= 1

        def move_to_head(self, node):
            self.remove_node(node)
            self.add_to_head(node)
        
        def pop_tail(self):
            if self.size == 0:
                return None
            node = self.tail.prev
            self.remove_node(node)
            return node

        

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.cache = {}
        self.freq_map = defaultdict(self.DoublyLinkedList)
    
    def _update_freq(self, node):
        old_freq = node.freq
        old_list = self.freq_map[old_freq]
        old_list.remove_node(node)

        if old_freq == self.min_freq and old_list.size == 0:
            self.min_freq += 1

        node.freq += 1
        self.freq_map[node.freq].add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._update_freq(node)
            return
        if self.size == self.capacity:
            node_to_remove = self.freq_map[self.min_freq].pop_tail()
            del self.cache[node_to_remove.key]
            self.size -= 1
        node = self.Node(key, value, 1)
        self.cache[key] = node
        self.freq_map[1].add_to_head(node)
        self.min_freq = 1
        self.size += 1
        return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)