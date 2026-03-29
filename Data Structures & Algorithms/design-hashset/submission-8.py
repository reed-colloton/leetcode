class ListNode:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.k = 1000
        self.buckets: list[ListNode | None] = [None] * self.k

    def _hash(self, key):
        return key % self.k

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        h = self._hash(key)
        node = self.buckets[h]
        if not node:
            self.buckets[h] = ListNode(key)
            return
        while node.next:
            node = node.next
        node.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        h = self._hash(key)
        node = self.buckets[h]
        prev = None
        while node:
            if node.key == key:
                if prev == None:
                    self.buckets[h] = node.next
                    return
                else:
                    prev.next = node.next
            prev = node
            node = node.next

    def contains(self, key: int) -> bool:
        node = self.buckets[self._hash(key)]
        while node:
            if node.key == key:
                return True
            node = node.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)