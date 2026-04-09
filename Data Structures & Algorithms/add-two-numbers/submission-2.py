# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = cur = ListNode()
        while l1 or l2 or carry:
            x = carry
            if l1:
                x += l1.val
                l1 = l1.next
            if l2:
                x += l2.val
                l2 = l2.next
            x1 = x % 10
            node = ListNode(x % 10)
            cur.next = node
            cur = node
            carry = x // 10
        return dummy.next