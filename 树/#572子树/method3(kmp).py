# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def get_nextval(s):
            nxt = [-1]
            x, now = 0, -1
            while x < len(s)-1:
                if now == -1 or s[x] == s[now]:
                    x += 1
                    now += 1
                    nxt.append(now)
                elif now:
                    now = nxt[now]
                else:
                    nxt.append(0)
                    x += 1
            return nxt
        # return if s1 contains s2
        def KMP(s1, s2):
            nxt = get_nextval(s2)
            i = j = 0
            while j < len(s2):
                if i >= len(s1):
                    return False

                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    i -= nxt[j]
                    j = 0
            return True
        # return tree list
        def dfs(t, lst):
            if not t: return
            lst.append(t.val)
            if t.left:
                dfs(t.left, lst)
            else:
                lst.append('l')
            if t.right:
                dfs(t.right, lst)
            else:
                lst.append('r')
        s1 = []
        s2 = []
        dfs(s, s1)
        dfs(t, s2)
        return KMP(s1, s2)



