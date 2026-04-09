# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2 or carry:
            x = carry

            if l1:
                x += l1.val
                l1 = l1.next
            if l2:
                x += l2.val
                l2 = l2.next
                
            carry = x // 10
            cur.next = ListNode(x % 10)
            cur = cur.next

        return dummy.next