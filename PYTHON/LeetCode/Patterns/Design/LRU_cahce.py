'''
    LC #146:
        NOTE:
            Approach 1: Takes advantage of existing puthon library ordered dict https://docs.python.org/3/library/collections.html#collections.OrderedDict
            Approach 2: Uses doubly linked list which has the benefit of constant time deletion and insertion in order
'''


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.tracker = 0
        self.map = dict()  # NOTE: Syntax Cannot use default dict because for some reason it saves values with default value when they are indexed

    def get(self, key: int) -> int:
        if key not in list(self.map.keys()):
            return -1

        self.tracker += 1
        value = self.map[key][1]
        self.map.update({key: (self.tracker, value, key)})

        return value

    def put(self, key: int, value: int) -> None:
        self.tracker += 1

        is_new = key not in list(
            self.map.keys())  # NOTE: Syntax If key aleady exists no need to incremenent count or pop if threshold met

        if self.count != self.capacity and is_new:
            self.count += 1
        elif self.count == self.capacity and is_new:
            values = list(self.map.values())
            heapq.heapify(
                values)  # NOTE: Syntax Need to call list on output of values. NOTE: Heapify transforms list in place
            poped_value = heapq.heappop(values)
            self.map.pop(poped_value[
                             2])  # NOTE: Library Need to delete from key from map. NOTE: Need to store key to delete afterwards. del map[key] also works

        self.map.update({key: (self.tracker, value, key)})

    # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)