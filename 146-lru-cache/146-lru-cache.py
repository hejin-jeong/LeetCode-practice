class LRUCache(object):
    import collections

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.recent = collections.deque()       

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.recent.remove(key)
            self.recent.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key] = value
            self.recent.remove(key)
            self.recent.append(key)
        elif len(self.cache) != self.capacity:
            self.cache[key] = value
            self.recent.append(key)
        elif len(self.cache) == self.capacity:
            least = self.recent.popleft()
            del self.cache[least]
            self.cache[key] = value
            self.recent.append(key)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)