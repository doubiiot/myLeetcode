# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        even = head.next
        odd_cur = head
        even_cur = even
        while even_cur and even_cur.next:
            odd_cur.next = even_cur.next
            even_cur.next = odd_cur.next.next
            odd_cur = odd_cur.next
            even_cur = even_cur.next
        odd_cur.next = even
        return head