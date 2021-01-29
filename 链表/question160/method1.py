# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = 0
        len_b = 0
        p_a = headA
        p_b = headB
        while(p_a):
            len_a += 1
            p_a = p_a.next
        while(p_b):
            len_b += 1
            p_b = p_b.next
        s = len_a - len_b
        out = None
        if(s <= 0):
            s = -s
            while(s):
                headB = headB.next
                s -= 1
            for j in range(len_a):
                if(headA == headB):
                    return headA
                headA = headA.next
                headB = headB.next
        else:
            while(s):
                headA = headA.next
                s -= 1
            for j in range(len_b):
                if(headA == headB):
                    return headA
                headA = headA.next
                headB = headB.next
        return out


