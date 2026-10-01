# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initialise left and right pointer to head
        # increment right pointer to the nth position
        # once the right pointer is n apart from the left,
        # increment them together (keeping the distance between them equal)
        # then when the right pointer gets to the end, we want to remove the left pointer
        
        right = head
        left = head
        distance = 0

        while distance < n:
            right = right.next
            distance +=1
        
        if right is None:
            head = head.next
            return head
        
        while right.next is not None:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return head
