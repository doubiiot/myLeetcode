# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        head = root
        list_len = 0
        while head:
            head = head.next
            list_len += 1
        '''
        len_per_group = list_len // k
        flag = list_len % k
        '''
        len_per_group, flag = divmod(list_len, k)
        ans = []
        dummy = ListNode(-1)
        dummy.next = root
        cur = dummy
        next_node = dummy.next

        for i in range(k):
            if next_node is None:
                ans.append(None)
            else:
                ans.append(next_node)
                for j in range(len_per_group + (i < flag)):
                    cur = cur.next
                    next_node = next_node.next
                '''
                if flag:
                    cur = cur.next
                    next_node = next_node.next
                    flag -= 1
                '''
                cur.next = None
                dummy.next = next_node
                cur = dummy
        return ans
