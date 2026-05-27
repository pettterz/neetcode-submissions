# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        curr = head
        while curr:
            total += 1
            curr = curr.next

        if total - n == 0:
             return head.next

        i = 0
        curr = head
        for i in range(total - 1):
            if (i + 1) == total - n:
                curr.next = curr.next.next
                break
            curr = curr.next


        return head
        