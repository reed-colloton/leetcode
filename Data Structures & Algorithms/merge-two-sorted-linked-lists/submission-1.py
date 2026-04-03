# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = end = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                tmp = list1
                list1 = list1.next
            else:
                tmp = list2
                list2 = list2.next
            tmp.next = None
            end.next = tmp
            end = end.next
        while list1:
            end.next = list1
            end = end.next
            list1 = list1.next
        while list2:
            end.next = list2
            end = end.next
            list2 = list2.next
        return start.next