class LRUCache(object):
    def __init__(self, capacity):
        self.ls = []
        self.c = capacity
        self.size = 0
        self.dict = {}
        """
        :type capacity: int
        """
    def get(self, key):
        if key in self.dict:
            i = self.ls.index(key)
            self.ls.pop(i)
            self.ls.append(key)
            return self.dict[key]
        else:
            return -1
        """
        :type key: int
        :rtype: int
        """
    def put(self, key, value):
        if key in self.dict:
            self.dict[key]=value
            i = self.ls.index(key)
            self.ls.pop(i)
            self.ls.append(key)
        elif self.c == self.size:
            tmpk = self.ls.pop(0)
            self.ls.append(key)
            self.dict.pop(tmpk)
            self.dict[key]=value
        else:
            self.ls.append(key)
            self.dict[key]=value
            self.size+=1
        """
        :type key: int
        :type value: int
        :rtype: void
        """
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)