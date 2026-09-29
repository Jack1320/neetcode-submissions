# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # walk through the linked list and ask if you have been at the current node before
        
        i = head
        seen = set()
        while i != None:
            if i in seen:
                return True
            else:
                seen.add(i)
            i = i.next
        return False
        