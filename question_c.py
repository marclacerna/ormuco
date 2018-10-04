import json


class GetFile:
    """
    Read/ Load json file, The jsons will contain geolocations
    """

    def __init__(self, path):
        self.path = path
        self.json_data = None
        self.ip_addr = None
        self.country = None
        self.city = None
        self.longlat = None

    def set_ip_addr(self, ip_addr):
        self.ip_addr = ip_addr

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_long_lat(self, longlat):
        self.longlat = longlat

    def read_json(self):
        with open(self.path, 'r') as read_file:
            self.json_data = json.load(read_file)

    def add_to_json(self, attrib):
        if attrib not in self.json_data:
            self.json_data[attrib] = list()
        else:
            self.json_data[attrib].append({'ip address': self.ip_addr,
                                           'country': self.country,
                                           'city': self.city,
                                           'long/lat': self.longlat})

            with open(self.path, 'w') as load_data:
                json.dump(load_data)


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
