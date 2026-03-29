class MyHashMap:

    def __init__(self):
        self.map = []

    def _find(self, key: int) -> int | None:
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                return i
        return None

    def put(self, key: int, value: int) -> None:
        index = self._find(key)
        if index != None:
            self.map[index] = (key, value)
        else:
            self.map.append((key, value))

    def get(self, key: int) -> int:
        index = self._find(key)
        if index == None:
            return -1
        return self.map[index][1]

    def remove(self, key: int) -> None:
        index = self._find(key)
        if index != None:
            self.map.remove((key, self.map[index][1]))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)