

class LRUCache:

    def __init__(self, capacity=0, ttl=0):
        self.capacity = capacity
        self.cache = dict()
        # need to add ttl logic
        self.ttl = ttl

    def insert_data(self, key, value):
        """
        Insert new items in the cache, remove first entry in
        the cache if its bigger than its capacity
        """
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            for k, v in enumerate(self.cache.keys()):
                if k == 0:
                    firstkey = v
                    break

            del self.cache[firstkey]

    def get_cache(self):
        return self.cache
