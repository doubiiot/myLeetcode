class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        list_len = 0
        head = root
        while head:
            head = head.next
            list_len += 1
        len_per_group, flag = divmod(list_len, k)

        ans = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(len_per_group + (i < flag)-1):
                if cur : cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans
