class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        self.root[key] = val
    def helper(self, key, prefix):
        n = 0
        l = len(key) - 1
        for i in prefix:
            if n > l or key[n] != i:
                return False
            n += 1
        return True
    def sum(self, prefix: str) -> int:
        rslt = 0
        for k,v in self.root.items():
            if self.helper(k, prefix):
                rslt += v
        return rslt
# 暴力法
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
