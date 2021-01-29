class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = quick = head
        while True:
            if not quick or not quick.next:
                return None
            slow, quick = slow.next, quick.next.next
            if slow == quick: break

        slow = head
        while slow != quick:
            slow, quick = slow.next, quick.next
        return slow
# O(n) O(1)
