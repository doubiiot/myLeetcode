# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#迭代一次 双指针
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = ListNode(-1)
        p.next = head
        r, s = p, p
        while n:
            s = s.next
            n -= 1
        while s.next != None:
            r = r.next
            s = s.next
        r.next = r.next.next
        return p.next





