# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#迭代
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prevnode = dummy

        while head and head.next:
            r = head
            s = head.next

            r.next = s.next
            s.next = r
            prevnode.next = s

            prevnode = r
            head = r.next

        return dummy.next