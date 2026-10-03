# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if lists == []:
            return None
        
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

        
        

        while len(lists) > 1:
            for i in range(len(lists)//2):
                j = i+1
                lists[i] = mergeTwoLists(lists[i], lists[j])
                del lists[j]
        return lists[0]

                