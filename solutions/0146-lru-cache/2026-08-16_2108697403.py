class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.recent(node)

        return node.value

    def remove(self, node: Node):
        prev = node.prev
        nxt = node.next

        nxt.prev = prev
        prev.next = nxt
    
    def recent(self, node:Node):
        recNode = self.head.next

        self.head.next = node
        recNode.prev = node

        node.next = recNode
        node.prev = self.head


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key,value)
        self.recent(node)

        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lastNode = self.tail.prev
            self.remove(lastNode)
            k = lastNode.key
            del self.cache[k]



            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)