# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        l = []
        len = 0
        while cur:
            l.append(cur.val)
            cur = cur.next
            len += 1
        if not len:
            return True
        else:
            for i in range(len // 2):
                if (l[i] != l[-(i + 1)]):
                    return False
            return True

