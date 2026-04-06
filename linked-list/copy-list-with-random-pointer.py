"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        node = head
        while node:
            node_next = node.next
            node_copy = Node(node.val, node_next)
            node.next = node_copy
            node = node_next
        head_copy = head.next
        node = head
        while node:
            node_copy = node.next
            if node.random:
                node_copy.random = node.random.next
            else:
                node_copy.random = None
            node = node_copy.next
        node = head
        while node:
            node_copy = node.next
            node_next = node.next.next
            node.next = node_next
            if node_next:
                node_copy.next = node_next.next
            else:
                node_copy.next = None
            node = node_next
        return head_copy

           