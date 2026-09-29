# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast is not None:
            fast = fast.next
            if fast is None:
                return False
            if fast == slow:
                return True
            fast = fast.next
            slow = slow.next

        return False
