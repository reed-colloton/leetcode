class ListNode:

    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self):
        return f'{self.key}: {self.value}'


class MyHashMap:

    def __init__(self):
        self.num_buckets = 10 * 1000
        self.map: list[ListNode] = [ListNode(None, None) for _ in range(self.num_buckets)]

    def __repr__(self) -> str:
        repr = '{\n'
        for node in self.map:
            while node.next != None:
                repr += f'  {node}\n'
                node = node.next
        return repr + '}'


    def _hash(self, key):
        return key % self.num_buckets


    def put(self, key: int, value: int) -> None:
        node = self.map[self._hash(key)]
        while node.next:
            if node.key == key:
                node.value = value
                return
            node = node.next
        self.map[self._hash(key)] = ListNode(key, value, node)


    def get(self, key: int) -> int:
        node = self.map[self._hash(key)]
        while node.next:
            if node.key == key:
                return node.value
            node = node.next
        return -1


    def remove(self, key: int) -> None:
        node = self.map[self._hash(key)]
        prev = None
        while node.next:
            if node.key == key:
                if prev == None:
                    self.map[self._hash(key)] = node.next
                else:
                    prev.next = node.next
                break
            prev = node
            node = node.next
