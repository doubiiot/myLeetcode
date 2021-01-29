class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        res = 1
        new_pairs = sorted(pairs, key = lambda x:x[1])
        pre_pair = new_pairs[0]
        for cur_pair in new_pairs:
            if cur_pair[0] > pre_pair[1]:
                res += 1
                pre_pair = cur_pair
        return res
# O(nlogn) O(n) 排序可能使用空间
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pre, res = float('-inf'), 0
        for cur_pair in sorted(pairs, key = lambda x:x[1]):
            if cur_pair[0] > pre:
                res += 1
                pre = cur_pair[1]
        return res
