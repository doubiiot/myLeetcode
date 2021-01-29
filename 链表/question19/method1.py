# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = ListNode(-1)
        p.next = head
        q = p
        o = p
        list_len = 0
        while p != None:
            list_len += 1
            p = p.next
        tmp = list_len - n - 1
        while tmp:
            q = q.next
            tmp -= 1
        q.next = q.next.next
        return o.next
