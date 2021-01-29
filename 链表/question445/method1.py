# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1,s2 = [],[]
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        #进位
        carry = 0
        #上一个节点
        ans = None
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()

            val = a + b + carry
            carry = val // 10
            val %= 10

            new_node = ListNode(val)
            new_node.next = ans
            ans = new_node
        return ans