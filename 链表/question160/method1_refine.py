# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#先到达统一起点，双指针齐头并进
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1 = headA
        cur2 = headB
        n = 0
        while cur1:
            n += 1
            cur1 = cur1.next
        while cur2:
            n -= 1
            cur2 = cur2.next
        if cur1 != cur2:
            return None
        # long
        cur1 = headA if n>0 else headB
        # short
        cur2 = headB if cur1 == headA else headA
        n = abs(n)
        while(n):
            cur1 = cur1.next
            n -= 1
        while(cur1):
            if(cur1 == cur2):
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
        return None


