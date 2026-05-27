# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = list1, list2

        head = ListNode()
        p = head

        while h1 and h2:
            if h1.val < h2.val:
                p.next = h1
                h1 = h1.next
            else:
                p.next = h2
                h2 = h2.next
            p = p.next

        p.next = h1 or h2

        return head.next
 

        