# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast.next is not None and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        new_head = slow.next
        slow.next = None
        
        # now reverse the second list
        curr, prev = new_head, None

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        tail = prev

        # interleave
        i = head
        j = tail

        while j is not None:
            i_nxt = i.next
            j_nxt = j.next
            i.next = j
            i.next.next = i_nxt
            j = j_nxt
            i = i_nxt