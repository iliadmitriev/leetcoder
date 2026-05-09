class Node:
    slots = ("key", "val", "prev", "next",)

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LinkedList:

    def __init__(self):
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node) -> None:
        """Remove node from double linked list.
        x - null

                prev     node     nxt
        left ->| n | -> | n | -> | n | -> x
           x <-| p | <- | p | <- | p | <- right
        
        """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert_right(self, node: Node) -> None:
        """Insert node to LRU before the right pointer.
        x - null

                prev     nxt       
        left ->| n | -> | n | -> x
           x <-| p | <- | p | <- right

                prev     node     nxt
        left ->| n | -> | n | -> | n | -> x
           x <-| p | <- | p | <- | p | <- right
        
        """
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt

    def get_left(self) -> Node:
        return self.left.next
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cache: Dict[int, Node] = {}
        self.capacity = capacity
        self.list = LinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.list.remove(node)
            self.list.insert_right(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.list.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.list.insert_right(node)

        if len(self.cache) > self.capacity:
            lru = self.list.get_left()
            self.list.remove(lru)
            del self.cache[lru.key]


