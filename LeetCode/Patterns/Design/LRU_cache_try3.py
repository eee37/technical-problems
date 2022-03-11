from collections import defaultdict


class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

    def print_node(self):
        node = self
        print_statement = 'start'
        while node is not None:
            print_statement += '->' + str(node.val)
            node = node.next
        print(print_statement + ' -> end')

class LRUCache:

    def __init__(self, capacity: int):
        self.nodemap = defaultdict(lambda: None)
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head 
        self.cap = capacity

    def print(self):
        print_statement = 'start'
        node = self.head
        while node.next is not None:
            print_statement += '->' + str(node.next.val)
            node = node.next
        print(print_statement)

    def get(self, key: int) -> int:
        if self.nodemap[key] is None:
            return -1
        node = self.nodemap[key]
        self.remove(node)
        self.maketail(node)
        # NOTE: Code clarity: Don't make any hashmap updates in fxns intended for linked list updates. Makes it hard to debug
        print(node.val)
        return node.val


    def put(self, key: int, value: int) -> None:
        node = self.nodemap[key]
        if node is not None:
            self.remove(node)
            node.val = value
            node.next = None
            node.prev = None
        else:
            if len(self.nodemap.keys()) > self.cap: # NOTE: Py method This doesnt work because default dictionary by default adds node to map when it doesnt  exist
                self.evict()
            node = Node(key, value)
        self.nodemap.update({node.key: node})
        self.maketail(node)
        
            
    # get rid of LRU
    def evict(self) -> None:
        if len(self.nodemap.keys()) == 0:
            return
        
        lru = self.head.next
        self.head.next = lru.next
        lru.next.prev = self.head
        
        del self.nodemap[lru.key]
        
    # remove node from linked list
    def remove(self, node) -> None:
        if node.key is None:
            return
        
        node.next.prev = node.prev
        node.prev.next = node.next
            
    def maketail(self, node) -> None:
        # clear 
        node.next = None
        node.prev = None
        
        node.next = self.tail
        node.prev = self.tail.prev
        
        self.tail.prev.next = node
        self.tail.prev = node
        
        
        
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(1)
# # obj.get(key)
# # obj.put(key,value)
# obj.put(2,1)
# obj.print()
# obj.get(2)
# obj.print()
# obj.put(3,2)
# obj.print()
# obj.get(3)
# obj.print()


obj = LRUCache(2)
# obj.get(key)
# obj.put(key,value)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
obj.put(3,3)
obj.get(2)
obj.put(4,4)
obj.get(1)
obj.get(3)
obj.get(4)
obj.print()