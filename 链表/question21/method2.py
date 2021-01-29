# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        preprev = ListNode(-1)
        p = preprev

        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l1.val <= l2.val:
                p.next = l1
                p = p.next
                p.next = self.mergeTwoLists(l1.next, l2)
            else:
                p.next = l2
                p = p.next
                p.next = self.mergeTwoLists(l1, l2.next)
            return preprev.next

