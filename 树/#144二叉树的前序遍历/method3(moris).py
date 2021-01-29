# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node, output = root, []
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right
        return output
# 左子树为空，输出node，新node为node的右子树
# 左子树非空，先往左走一步，然后到最右的节点(pre_right)：
    # pre_right右子树为空：
        # 输出node
        # pre_right.right指向node
        # node = node.left
    # pre_right右子树不为空：
        # 置空
        # 新node为node.right
# time O(N)
# space O(N)