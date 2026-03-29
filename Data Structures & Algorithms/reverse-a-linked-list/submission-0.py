# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == []:
            return head
        reversed_head = None
        while head != None:
            next = head.next
            head.next = reversed_head
            reversed_head = head
            head = next
        return reversed_head
