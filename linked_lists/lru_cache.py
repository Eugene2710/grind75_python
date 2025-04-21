from typing import Optional


# 1105
class Node:
    def __init__(self, key: int, val: int, next: "Node" | None = None, prev: "Node" | None = None) -> None:
        self.key: int = key
        self.val: int = val
        self.next: "Node" | None = next
        self.prev: "Node" | None = prev


class LRUCache:
    """
    Hashmap with int as key, pointer to doubly linked list nodes as value
    keep track of capacity
    extreme left pointer is LRU, extreme right pointer is most recently used

    time complexity: O(1)
    space complexity: O(cap)
    """
    def __init__(self, capacity: int) -> None:
        self.cache: dict[int | None, None | None] = {} # hashmap where key is int, and value is pointer to Node
        self.cap: int = capacity

        self.left: Node = Node(0,0) # dummy pointer for LRU node
        self.right: Node = Node(0,0) # dummy pointer for most recently used node
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node) -> None:
        """
        helper function to cut off and extend pointers of node.prev to node.next and vice versa
        """
        prev: Node = node.prev
        nxt: Node = node.next
        prev.nxt = nxt
        nxt.prev = prev

    def insert(self, node) -> None:
        """
        change previously self.right.prev.next to node and self.right.prev to node
        """
        tmp: Node = self.right.prev
        tmp.next = node
        node.prev = tmp
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        """
        check if key exists, if it exists:
            remove node -> insert node into cache as value and its key to self.right
            return 1
        else:
            return -1
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        """
        self.insert node into self.right.prev
        if length of self.cache is longer than capacity, remove self.left.next
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru: Node = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
