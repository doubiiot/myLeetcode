class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        dic = {0: 1}

        def dfs(root, dic, cur_sum):
            if not root:
                return 0
            cur_sum += root.val
            pre = cur_sum - sum
            # 函数返回指定键的值，如果值不在字典中返回默认值。
            num = dic.get(pre, 0)

            dic[cur_sum] = dic.get(cur_sum, 0) + 1
            num_left = dfs(root.left, dic, cur_sum)
            num_right = dfs(root.right, dic, cur_sum)
            # 重置是为了回到上一层，回到根节点，然后再才从右子树继续
            # 删除当前点的路径和信息 返回上一层
            dic[cur_sum] = dic.get(cur_sum, 0) - 1
            return num + num_left + num_right
        return dfs(root, dic, 0)
