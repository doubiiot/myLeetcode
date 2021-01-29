class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

dummy = ListNode(-1)
cur = dummy
head = dummy
node_list = [1,2,3,4,5,6]
for i in range(len(node_list)):
    new_node = ListNode(node_list[i])
    cur.next = new_node
    cur = cur.next
dummy.next, dummy = None, dummy.next
print(head.val)
print(head.next)
print(dummy.val)
print(dummy.next.val)