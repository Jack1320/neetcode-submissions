# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        dummy = list3

        i = list1
        j = list2

        while i is not None and j is not None:
            if i.val < j.val:
                dummy.next = i
                dummy = dummy.next
                i = i.next
            else:
                dummy.next = j
                dummy = dummy.next
                j = j.next
        if i is None and j is not None:
            dummy.next = j
        elif i is not None and j is None:
            dummy.next = i
        return list3.next