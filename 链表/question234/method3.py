# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse_list(self, head):
        cur = head
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        else:
            quick, slow = head, head
            l = head
            while quick.next is not None and quick.next.next is not None:
                quick = quick.next.next
                slow = slow.next
            l_revrs = self.reverse_list(slow.next)
            while l_revrs:
                if l_revrs.val != l.val:
                    return False
                l_revrs = l_revrs.next
                l = l.next
            return True



