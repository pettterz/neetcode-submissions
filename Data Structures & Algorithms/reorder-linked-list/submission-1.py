# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        sec = slow.next
        prev = None
        slow.next = None

        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec = tmp

        fst = head
        sec = prev

        while sec:
            t1, t2 = fst.next, sec.next
            fst.next = sec
            sec.next = t1
            fst, sec = t1, t2

        






        