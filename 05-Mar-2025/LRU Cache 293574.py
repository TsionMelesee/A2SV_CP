# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key=-1, value=-1, next=None, prev=None):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pointers = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.pointers:
            node = self.pointers[key]
            self.remove(node)
            self.insertAtTail(node)
            return node.val
        return -1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.pointers[node.key]

    def insertAtTail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.pointers[node.key] = node
        
    def put(self, key: int, value: int) -> None:
        if key in self.pointers:
            node = self.pointers[key]
            node.val = value
            self.remove(node)
        else:
            if len(self.pointers) == self.capacity:
                self.remove(self.head.next)
            node = Node(key, value)
        self.insertAtTail(node)
