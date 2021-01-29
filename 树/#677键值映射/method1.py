class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for i in key:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
        cur['val'] = val

    def get_sum(self, node_dic):
        rslt = 0
        for k, v in node_dic.items():
            if k == 'val':
                rslt += v
            else:
                rslt += self.get_sum(node_dic[k])
        return rslt

    def sum(self, prefix: str) -> int:
        cur = self.root
        rslt = 0
        for i in prefix:
            if i not in cur:
                return 0
            cur = cur[i]
        rslt = self.get_sum(cur)
        return rslt

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# 自己做的前缀树方法
