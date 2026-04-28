# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        dummy = tail = ListNode()
        while node:
            tmp = node
            start, end = self.reverse(node, k)
            node = end
            tail.next = start
            tail = tmp
        return dummy.next

    @staticmethod
    def reverse(node, k):
        rev = None
        cur = node
        for _ in range(k - 1):
            if not cur.next:
                return node, None
            cur = cur.next
        for _ in range(k):
            tmp = node.next
            node.next = rev
            rev = node
            node = tmp
        return rev, node # new start, next node
