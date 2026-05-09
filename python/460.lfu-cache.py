class Node:
    """Double linked list Node."""
    slots = ('value', 'prev', 'next')
    
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.next, self.prev = nxt, prev

    def __repr__(self):
        name = self.__class__.__name__
        return f"{name}(value={self.value}, prev={bool(self.prev)}, next={bool(self.next)})"


class DLinkedList:
    def __init__(self):
        # sentinel dummy nodes
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next, self.right.prev = self.right, self.left
        # type: Dict[int, Node]
        self.nodes = {}

    def __repr__(self):
        res = []
        node = self.left.next
        while node != self.right:
            res.append(node)
            node = node.next
        data = ' -> '.join(map(str, res))
        return f"{self.__class__.__name__}({data})"

    def __len__(self):
        return len(self.nodes)

    def push_right(self, val):
        # create node and add it to HashMap linking prev and next links
        node = Node(val, self.right.prev, self.right)
        self.nodes[node.value] = node
        # link right sentinel previous pointer to recently added node 
        self.right.prev = node
        # link next pointer of previous right node to a new right node
        node.prev.next = node

    def pop(self, val):
        if val in self.nodes:
            node = self.nodes[val]
            nxt, prev = node.next, node.prev
            prev.next, nxt.prev = nxt, prev
            self.nodes.pop(val, None)

    def pop_left(self):
        val = self.left.next.value
        self.pop(val)
        return val

    def update(self, val):
        self.pop(val)
        self.push_right(val)


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu_count = 0
        # map key -> val
        self.value_map = {}
        # map key -> count
        self.count_map = collections.defaultdict(int)
        # map key -> double linked list
        self.list_map = collections.defaultdict(DLinkedList)

    def counter(self, key):
        cnt = self.count_map[key]
        self.count_map[key] += 1
        self.list_map[cnt].pop(key)
        self.list_map[cnt + 1].push_right(key)

        if cnt == self.lfu_count and len(self.list_map[cnt]) == 0:
            self.lfu_count += 1

    def get(self, key: int) -> int:
        if key not in self.value_map:
            return -1
        self.counter(key)
        return self.value_map[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.value_map and len(self.value_map) == self.capacity:
            res = self.list_map[self.lfu_count].pop_left()
            self.value_map.pop(res)
            self.count_map.pop(res)

        self.value_map[key] = value
        self.counter(key)
        self.lfu_count = min(self.lfu_count, self.count_map[key])
