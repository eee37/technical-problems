from collections import defaultdict
'''
    NOTE: 
        SOLUTION:
            1. Need a dummy node for tail o.w things fall apart
'''

class Node:
    def __init__(self, key_value):
        self.val = key_value
        self.prev = None
        self.next = None
    
    def print_node(self):
        node = self
        print_statement = 'start -> '
        while node is not None:
            print_statement += '->' + str(node.val)
            node = node.next
        print(print_statement + ' -> end')

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = defaultdict(lambda: None)
        self.cap = capacity
        self.start = Node(None) # Dummy node
        self.tail = self.start
    
    def print(self):
        print_statement = 'start -> '
        node = self.start
        while node.next is not None:
            print_statement += '->' + str(node.next.val)
            node = node.next
        print(print_statement + ' -> end')

    def get(self, key: int) -> int:
        if self.hashmap[key] is not None:
            node = self.hashmap[key]
            # remove node
            self.remove(node)
            # update tail
            self.updatetail(node)
            return node.val[1]
        return -1
        

    def put(self, key: int, value: int) -> None:
        # remove node if needed NOTE: Needs to be done first if done after hashmap created will always excecute and will fail bc nodes pointers don't get updated till updatetail
        if self.hashmap[key] is not None:
            self.remove(self.hashmap[key])
        # create new node
        new_node = Node((key, value))
        self.hashmap.update({key: new_node})
        # remove LRU if needed
        if len(self.hashmap.keys()) > self.cap and self.start.next is not None:
            del self.hashmap[self.start.next.val[0]]
            self.remove(self.start.next)
        # update tail
        self.updatetail(new_node)
        
        

    def remove(self, node) -> None:
        if node:
            node.prev.next = node.next # NOTE: Here we are resetting head to None after adding a new node
            if node.next is not None:
                node.next.prev = node.prev
            
    def updatetail(self, node) -> None:
        self.tail.next = node # NOTE: Issue exits here. When current node already tail and getting updated
        node.prev = self.tail # NOTE: Issttue exits here. When you update tail you will also update this nodes prev pointer. tail gets updated below. Turns out its easier to just create a dummy for tail as well
        node.next = None
        self.tail = node
        
        
        
# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)
# obj.get(key)
# obj.put(key,value)
obj.put(2,1)
obj.print()
obj.get(2)
obj.print()
obj.put(3,2)
obj.print()
obj.get(3)
obj.print()