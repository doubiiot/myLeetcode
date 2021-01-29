# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_right(head):
            right = 0
            while head:
                head = head.next
                right += 1
            return right
        def build_bst(left, right):
            if left > right: return None
            mid = (left + right) // 2
            root = TreeNode()
            root.left = build_bst(left, mid-1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = build_bst(mid+1, right)
            return root
        right = get_right(head)
        node = build_bst(0, right-1)
        return node
# Time O(N) space O(logN)
