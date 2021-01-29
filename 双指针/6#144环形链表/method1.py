# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        cur1, cur2 = head, head
        flag = 0
        while cur2:
            if not cur2.next:
                return False
            if cur1.val == cur2.val and flag:
                return True
            else:
                cur1 = cur1.next
                cur2 = cur2.next.next
                flag = 1
        return False
# 双指针做法
# O(N) O(1)