# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        r, s = head, head
        for i in range(n):
            s = s.next
        if not s:
            return head.next
        else:
            while s.next:
                r = r.next
                s = s.next
            r.next = r.next.next
            return head





