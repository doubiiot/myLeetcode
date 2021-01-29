# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.p = head

        def func(cur=head):
            # cur is none
            if cur:
                if not func(cur.next):
                    return False
                if self.p.val != cur.val:
                    return False
                self.p = self.p.next
            return True

        return func()

